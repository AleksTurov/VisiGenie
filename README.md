# VisiGenie 🎨🤖
**VisiGenie** is a Telegram bot that generates images and videos based on text descriptions using models from Hugging Face and AWS cloud services. The project is designed to demonstrate AI capabilities in natural language processing and content generation using free-tier options.

## 📌 Key Features
- 🔮 Generate images based on text prompts using Diffusion models from Hugging Face.
- 🎥 Create short videos based on text descriptions.
- 🤖 Interactive chat via Telegram using the `python-telegram-bot` library.
- ☁️ Store and process data using AWS (S3 for files and Lambda for functions).

---

## 🚀 Technologies
- **Python 3.10+**: main programming language.
- **Hugging Face Transformers**: for loading and working with models.
- **AWS S3 and Lambda**: for data storage and processing.
- **python-telegram-bot**: library for building Telegram bots.
- **FFmpeg**: for video processing (if needed).
- **Docker**: for containerizing the application.
- **FastAPI**: for building REST APIs (if required).
- **MLflow**: for tracking experiments and model versions (in the future).

---

## 📦 Installation and Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/username/VisiGenie.git
   cd VisiGenie
