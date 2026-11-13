import os
import requests
from dotenv import set_key
from dotenv import load_dotenv

ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(ENV_PATH)

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
company_id = os.getenv("ID_COMPANY")

if not all([login, password, company_id]):
    raise RuntimeError("Нужны LOGIN, PASSWORD и ID_COMPANY в .env")

base_url = "https://ru.yougile.com"
creds = {
    "login": login,
    "password": password,
    "companyId": company_id,
}

resp = requests.post(f"{base_url}/api-v2/auth/keys", json=creds)
resp.raise_for_status()

data = resp.json()
if "key" not in data:
    raise RuntimeError(f"В ответе нет поля 'key': {data}")

token = data["key"]
set_key(ENV_PATH, "API_TOKEN", token)

print(f"[OK] API_TOKEN успешно записан в {ENV_PATH}")
