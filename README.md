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

В консоли будет показыватся ошибка с этим файлом если она будет. Если он загружен. то выведит ```Uploaded data-1.jpg```


### Ошибки

```data-uploader-1  | Bucket already exists or failed: An error occurred (BucketAlreadyOwnedByYou) when calling the CreateBucket operation: Your previous request to create the named bucket succeeded and you already own it.``` - Бакет уже создан

```Failed to upload data-4.jpg: [Errno 2] No such file or directory: 'data-4.jpg'``` - Кончились или нет файла

```Failed to upload data-50.txt: Failed to upload data-50.txt to test-bucket/data-50.txt: An error occurred (IncompleteBody) when calling the PutObject operation: You did not provide the number of bytes specified by the Content-Length HTTP header.```- Место кончилось или проблема интернета

### в определённой ситуации получается пробивать квоту бакета - почему?

На стадии прогерства заметил, что когда добавляю файлики по 1 мб каждую секунду, число общего мегабайт увеличивается со временем. Возможно из-за этого Minio не успевает просто обработать сумму обьема всех файлов, и обходит лимит. Как я понял, чтобы проверить лимит, он анализирует все занаво. Если в момент проскрчить, когда квота не прывышена и анализ не закончился, то за счет этого может быть превышение квоты