import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.load_model_from_huggingface import aws_access_key_id, aws_secret_access_key
import boto3
bucket_name = 'my-new-bucket-aturov'  # Укажите название вашего S3 бакета

def download_file_from_s3(bucket_name, object_name, download_path):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    
    try:
        s3_client.download_file(bucket_name, object_name, download_path)
        print(f"Файл {object_name} успешно скачан в {download_path}.")
    except Exception as e:
        print(f"Ошибка при скачивании файла: {e}")

# Пример скачивания файла
download_file_from_s3(bucket_name, 'random_test_file.txt', 'downloaded_random_test_file.txt')
