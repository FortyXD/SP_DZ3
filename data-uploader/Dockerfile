FROM python:3.9-slim

WORKDIR /app
COPY uploader.py .
COPY data-1.jpg .
COPY data-2.jpg .
COPY data-3.jpg .

RUN pip install boto3

CMD ["python", "uploader.py"]
