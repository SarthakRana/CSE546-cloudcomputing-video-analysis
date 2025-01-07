#__copyright__   = "Copyright 2024, VISA Lab"
#__license__     = "MIT"

import os
import logging
from boto3 import client as boto3_client
from face_recognition_code import face_recognition_function


s3 = boto3_client('s3')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):	
	logger.info('inside handler')
	image_bucket_name = event['bucket_name']
	image_file_name = event['image_file_name']
	output_bucket_name = 'output'
	data_bucket_name = 'data-file'
	data_file_name = 'data.pt'
	
	# downloading data.pt file from s3
	s3.download_file(data_bucket_name, data_file_name, f'/tmp/{data_file_name}')

	# downloading image file from s3
	image_file_path = f'/tmp/{image_file_name}'
	s3.download_file(image_bucket_name, image_file_name, image_file_path)

	response_name = face_recognition_function(image_file_path)

	output_txt_file_name = image_file_name.split('.')[0]
	# uploading output txt file to s3
	logger.info(f'output text file name {output_txt_file_name}.txt')
	with open(f'/tmp/{output_txt_file_name}.txt', 'rb') as f:
		s3.put_object(Body=f, Bucket=output_bucket_name, Key=f'{output_txt_file_name}.txt')

	logger.info(f'response name {response_name}')