# CSE546-cloudcomputing-video-analysis

This project is part of CSE546: Cloud Computing course take at ASU in Fall 24. I successfully developed and deployed a serverless video analysis pipeline on AWS that showcases the power of modern cloud architectures. The project leverages AWS Lambda for automatic scaling and cost-effectiveness – exactly what today's cloud-native applications demand.


![](https://github.com/SarthakRana/CSE546-cloudcomputing-video-analysis/blob/main/architecture.png)


## 🛠️ 𝗔𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲 & 𝗜𝗺𝗽𝗹𝗲𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻:

 👉 Input Processing:
- Implemented automated triggering of Lambda functions on video uploads to S3.
- Built a video-splitting function using FFmpeg to extract key frames.
- Orchestrated seamless data flow between processing stages.

 👉 Face Recognition Pipeline:
- Developed a sophisticated face detection system using Single Shot MultiBox Detector (SSD)
- Integrated ResNet-34 CNN model for accurate face recognition
- Optimized container images for Lambda deployment, significantly reducing deployment size
- Implemented asynchronous function chaining for improved performance

## 🎓 𝗞𝗲𝘆 𝗧𝗲𝗰𝗵𝗻𝗶𝗰𝗮𝗹 𝗛𝗶𝗴𝗵𝗹𝗶𝗴𝗵𝘁𝘀:

✅ Built a multi-stage video processing pipeline using AWS Lambda functions

✅ Implemented face recognition using ResNet-34 and SSD for accurate detection

✅ Utilized FFmpeg for video frame extraction

✅ Orchestrated data flow between functions using S3 buckets

✅ Successfully processed 100-video workload within 300 seconds🚀 

✅ Achieved efficient scaling under load while maintaining cost-effectiveness

✅ Achieved 95%+ accuracy in face recognition 🎯 

The project demonstrated how modern cloud architectures can efficiently handle complex ML workloads. It's a perfect example of combining serverless computing, machine learning, and automation to create scalable solutions.
