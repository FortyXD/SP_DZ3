import boto3
import os
from time import sleep

# Данные подключения к MiniO
S3_ENDPOINT = "http://minio:9000"
ACCESS_KEY = "admin"
SECRET_KEY = "admin123"
BUCKET_NAME = "test-bucket"


print("Start Work")
s3 = boto3.client(
    "s3",
    endpoint_url=S3_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

try:
    s3.create_bucket(Bucket=BUCKET_NAME)
    print(f"Bucket {BUCKET_NAME} created!")
except Exception as e:
    print(f"Bucket already exists or failed: {e}")

i = 1
while True:
    file_name = f"data-{i}.jpg"
    try:
        s3.upload_file(file_name, BUCKET_NAME, file_name)
        print(f"Uploaded {file_name}")
    except Exception as e:
        print(f"Failed to upload {file_name}: {e}")
        break

    os.remove(file_name)
    i += 1
    sleep(1)
