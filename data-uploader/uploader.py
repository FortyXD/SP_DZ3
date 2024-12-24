import subprocess
import boto3
import os
from time import sleep

S3_ENDPOINT = "http://minio:9000"
ACCESS_KEY = "admin"
SECRET_KEY = "admin123"
BUCKET_NAME = "test-bucket"
QUOTA = "50MiB"


def runproc(command):
    process = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.returncode != 0:
        print(f"Error running command")
    else:
        print(f"Command executed successfully: {process.stdout}")
    return process


def set_quote():
    sleep(3)
    runproc([
        "mc", "alias", "set", "myminio", S3_ENDPOINT, ACCESS_KEY, SECRET_KEY
    ])

    runproc([
        "mc", "quota", "set", f"myminio/{BUCKET_NAME}", "--size", QUOTA
    ])
    print(f"Bucket '{BUCKET_NAME}' quota set to {QUOTA}.")


def main():
    print("Start Work")

    s3 = boto3.client(
        "s3",
        endpoint_url=S3_ENDPOINT,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
    )

    try:
        s3.create_bucket(Bucket=BUCKET_NAME)
        print(f"Bucket {BUCKET_NAME} created")
    except Exception as e:
        print(f"Bucket already exists or failed: {e}")

    set_quote()

    i = 1
    while True:
        file_name = f"data-{i}.jpg"

        # для проверки overflow

        # file_name = f"data-{i}.txt"
        # with open(file_name, "w") as f:
        #     f.write("X" * 1024 * 1024)

        try:
            s3.upload_file(file_name, BUCKET_NAME, file_name)
            print(f"Uploaded {file_name}")
            os.remove(file_name)

        except Exception as e:
            print(f"Failed to upload {file_name}: {e}")
            break

        i += 1
        sleep(1)


if __name__ == "__main__":
    main()
