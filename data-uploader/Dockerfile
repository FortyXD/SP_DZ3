FROM python:3.9-slim

RUN apt-get update && apt-get install -y wget && \
    wget https://dl.min.io/client/mc/release/linux-amd64/mc -O /usr/local/bin/mc && \
    chmod +x /usr/local/bin/mc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

# Ставим необходимые Python-библиотеки
RUN pip install --no-cache-dir boto3

CMD ["python", "uploader.py"]
