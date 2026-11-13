import os
import requests
from dotenv import load_dotenv, set_key

# Путь к .env относительно этого скрипта
ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")

# Загружаем переменные, чтобы взять логин/пароль
load_dotenv(ENV_PATH)

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

if not login or not password:
    raise RuntimeError(
        "Не заданы LOGIN и/или PASSWORD в .env. Сначала пропиши их вручную.")

base_url = "https://ru.yougile.com"
creds = {"login": login, "password": password}

resp = requests.post(f"{base_url}/api-v2/auth/companies", json=creds)
resp.raise_for_status()

data = resp.json()
if "content" not in data or len(data["content"]) == 0:
    raise RuntimeError("В ответе API нет списка компаний: " + str(data))

company_id = data["content"][0]["id"]

# Записываем ТОЛЬКО чистое значение (строку)
set_key(ENV_PATH, "ID_COMPANY", str(company_id))

print(f"[OK] ID компании {company_id} успешно записан в {ENV_PATH}")
