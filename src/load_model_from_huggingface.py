from dotenv import load_dotenv
import os
from huggingface_hub import HfApi

# Загружаем переменные окружения из .env файла в корневой директории проекта
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Получаем токены из переменных окружения
telegram_api_token = os.getenv("TELEGRAM_API_TOKEN")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
hf_api_token = os.getenv("HUGGINGFACE_API_TOKEN")

# Проверка, если токены не найдены
if telegram_api_token is None:
    raise ValueError("Telegram API Token is not set in .env file")
if aws_access_key_id is None:
    raise ValueError("AWS Access Key ID is not set in .env file")
if aws_secret_access_key is None:
    raise ValueError("AWS Secret Access Key is not set in .env file")
if hf_api_token is None:
    raise ValueError("HuggingFace API Token is not set in .env file")

# Теперь токены можно использовать в вашем коде
print("Telegram API Token:", telegram_api_token)
print("AWS Access Key ID:", aws_access_key_id)
print("HugginFace API Token:", hf_api_token)

# Использование токена Hugging Face для загрузки модели
api = HfApi(token=hf_api_token)
model = api.model_info("bert-base-uncased")
print(model)