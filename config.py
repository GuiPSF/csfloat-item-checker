import os
from dotenv import load_dotenv

load_dotenv()

API_KEY: str | None = os.getenv("API_KEY")
BASE_URL: str | None = os.getenv("BASE_URL")

if not API_KEY or not BASE_URL:
    raise EnvironmentError("API_KEY ou BASE_URL não configurados")
