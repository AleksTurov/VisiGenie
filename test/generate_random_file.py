# Генерация случайного контента
import random
import string
import boto3
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# Загружаем переменные окружения из .env файла в корневой директории проекта
from src.load_model_from_huggingface import aws_access_key_id, aws_secret_access_key


def generate_random_file(file_name, file_size_mb=1):
    """Генерация случайного файла указанного размера (в МБ)"""
    with open(file_name, 'w') as f:
        random_content = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size_mb * 1024 * 1024))
        f.write(random_content)

file_name = 'random_test_file.txt'
bucket_name = 'my-new-bucket-aturov'  # Укажите название вашего S3 бакета
generate_random_file(file_name)

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

# Загрузка в S3
upload_file_to_s3(file_name, bucket_name, file_name)
