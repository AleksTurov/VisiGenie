import boto3
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# Загружаем переменные окружения из .env файла в корневой директории проекта
from src.load_model_from_huggingface import aws_access_key_id, aws_secret_access_key

bucket_name = 'my-new-bucket-aturov'  # Укажите название вашего S3 бакета
def delete_file_from_s3(bucket_name, object_name):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        print(f"Файл {object_name} удален из бакета {bucket_name}.")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")

# Пример удаления файла
delete_file_from_s3(bucket_name, 'random_test_file.txt')
