import os
from dotenv import load_dotenv
from telegram import Bot
from telegram.error import TelegramError
import boto3
from botocore.exceptions import NoCredentialsError

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем токены из переменных окружения
telegram_api_token = os.getenv("TELEGRAM_API_TOKEN")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

# Проверка, что токены правильно загружены
if not telegram_api_token or not aws_access_key_id or not aws_secret_access_key:
    print("Ошибка: Не все токены загружены! Проверьте файл .env.")
    exit(1)

# 1. Отправка сообщения в Telegram
def send_telegram_message(chat_id, message):
    bot = Bot(token=telegram_api_token)
    try:
        bot.send_message(chat_id=chat_id, text=message)
        print("Сообщение успешно отправлено в Telegram!")
    except TelegramError as e:
        print(f"Ошибка при отправке сообщения: {e}")

# 2. Загрузка файла в S3
def upload_file_to_s3(file_path, bucket_name, object_name):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"Файл {file_path} успешно загружен в S3 в бакет {bucket_name}!")
    except NoCredentialsError:
        print("Ошибка: Неверные учетные данные AWS!")
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")

# Основная логика
if __name__ == "__main__":
    # Пример отправки сообщения в Telegram
    telegram_chat_id = "your_chat_id"  # Замените на ваш chat_id
    send_telegram_message(telegram_chat_id, "Привет, это тестовое сообщение от бота!")

    # Пример загрузки файла в S3
    file_path = "path_to_your_file"  # Укажите путь к вашему файлу
    bucket_name = "your_bucket_name"  # Укажите название вашего S3 бакета
    object_name = "your_file_key"  # Укажите ключ для файла в S3
    upload_file_to_s3(file_path, bucket_name, object_name)
