import boto3
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# Загружаем переменные окружения из .env файла в корневой директории проекта
from src.load_model_from_huggingface import aws_access_key_id, aws_secret_access_key
bucket_name = 'my-new-bucket-aturov'  # Укажите название вашего S3 бакета

def list_files_in_s3(bucket_name):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f"Файл: {obj['Key']}, Размер: {obj['Size']} байт")
        else:
            print("Бакет пуст.")
    except Exception as e:
        print(f"Ошибка при списке файлов: {e}")

# Проверка содержимого бакета
list_files_in_s3(bucket_name)
