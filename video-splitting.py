import os
import json
import boto3
import logging
import subprocess
logger=logging.getLogger()
logger.setLevel(logging.INFO)

INPUT_BUCKET = "1229424068-input"
DESTINATION_BUCKET = "1229424068-stage-1"

s3_client = boto3.client('s3')


def video_splitting_cmdline(video_filename):
    # Get the base filename without extension
    filename = os.path.basename(video_filename)
    base_name = os.path.splitext(filename)[0]
    # Create output directory
    output_dir = f'/tmp/{base_name}'
    os.makedirs(output_dir, exist_ok=True)
    # split the frames
    split_cmd = f'/opt/bin/ffmpeg -ss 0 -r 1 -i {video_filename} -vf fps=1/10 -start_number 0 -vframes 10 {output_dir}/output_%02d.jpg -y'
    try:
        subprocess.check_call(split_cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print(e.returncode)
        print(e.output)
    return output_dir


def upload_to_s3(local_folder):
    # Get the base folder name
    folder_name = os.path.basename(os.path.normpath(local_folder))
    uploaded_files = []
    
    logger.info(f"Starting upload of folder {folder_name} to bucket {DESTINATION_BUCKET}")
    
    # Walk through the directory
    for root, dirs, files in os.walk(local_folder):
        for filename in files:
            # Get the full local path
            local_path = os.path.join(root, filename)
            
            # Create S3 key (path in bucket)
            # Remove '/tmp/' from the path and construct the S3 key
            relative_path = os.path.relpath(local_path, '/tmp')
            s3_key = relative_path
            
            logger.info(f"Uploading {local_path} to {s3_key}")
            
            # Upload file to S3
            try:
                with open(local_path, 'rb') as file_obj:
                    s3_client.upload_fileobj(file_obj, DESTINATION_BUCKET, s3_key)
                uploaded_files.append(s3_key)
                logger.info(f"Successfully uploaded {s3_key}")
            except Exception as e:
                logger.error(f"Error uploading {filename}: {str(e)}")
                raise
 

def lambda_handler(event, context):
    try:
        filename = event['Records'][0]['s3']['object']['key']
        s3_client = boto3.client('s3')
        download_path = '/tmp/' + filename
    
        s3_client.download_file(INPUT_BUCKET, filename, download_path)
        print(f"video downloaded successfully at {download_path}")
        
        output_dir = video_splitting_cmdline(download_path)
        logger.info(f"output folder {output_dir}")
        print("video splitted successfully")
        # Get list of generated frames
        frames = sorted([f for f in os.listdir(output_dir) if f.endswith('.jpg')])
        logger.info(f"Generated {len(frames)} frames: {frames}")
        # Upload folder to stage-1 s3 bucket
        upload_to_s3(output_dir)
        return {
            'statusCode': 200,
            'body': json.dumps('Video splitted and uploaded successfully')
        }
    
    except Exception as e:
        print(f"Error: {e}")