# Дз по спецкурсу номер 3
Задание выполненно Моисейкиным Андреем 202 группа
### Приготовление

Все тестировалось на mac os. Для запуска нужно установить Docker desktop, затем прописать прописать команду:

```docker compose up --build```

Для удаления контейнера нужно прописать команду:

```docker compose down```

Должна быть папка дир, где будут находится все основные данные minio

### Добавление и удаление файлов через скрипт питона

Чтобы добавить автоматически фото, нужно через Dockerfile в папке /data-uploader
Добавить файл с именем data-{index}.jpg
```COPY data-3.jpg .```

В консоли будет показыватся ошибка с этим файлом если она есть. Если он загружен. то выведит ```Uploaded data-1.jpg```


### Ошибки

```data-uploader-1  | Bucket already exists or failed: An error occurred (BucketAlreadyOwnedByYou) when calling the CreateBucket operation: Your previous request to create the named bucket succeeded and you already own it.``` - Бакет уже создан

```Failed to upload data-4.jpg: [Errno 2] No such file or directory: 'data-4.jpg'``` - Кончились или нет файла

```Failed to upload data-50.txt: Failed to upload data-50.txt to test-bucket/data-50.txt: An error occurred (IncompleteBody) when calling the PutObject operation: You did not provide the number of bytes specified by the Content-Length HTTP header.```- Место кончилось или проблема интернета