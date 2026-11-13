import os
import pytest
import requests
from dotenv import load_dotenv

ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(ENV_PATH)

base_url = "https://ru.yougile.com"


@pytest.fixture(scope="session")
def company_id():
    cid = os.getenv("ID_COMPANY")
    if not cid:
        raise RuntimeError(
            "ID_COMPANY не найден. Запустите setup_company_id.py вручную.")
    return cid


@pytest.fixture(scope="session")
def api_token():
    token = os.getenv("API_TOKEN")
    if token:
        return token
    # Если токена нет, можно либо требовать его наличие, либо генерировать
    # один раз
    # (но лучше требовать наличие и обновлять вручную через setup_token.py)
    raise RuntimeError(
        "API_TOKEN не найден. Запустите setup_token.py вручную"
        "или задайте через переменные окружения.")


@pytest.fixture(scope="session")
def project_id(api_token):
    my_headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    # Лучше делать уникальное название,
    # иначе при повторном запуске будет конфликт
    import uuid
    title = f"Трубопровод Главный {uuid.uuid4()}"
    payload = {'title': title}

    resp = requests.post(
        base_url + '/api-v2/projects',
        json=payload,
        headers=my_headers
    )

    # Всегда лучше raise_for_status(),
    # чем assert — сообщение об ошибке понятнее
    resp.raise_for_status()
    data = resp.json()
    print("Полный ответ API:", data)

    pid = data["id"]
    print(f"[FIXTURE] Создан проект с ID: {pid}")

    yield pid  # <-- Это ключевая строка: отдаём ID тестам

    # Блок после yield — это очистка (
    # выполнится после всех тестов, использующих эту фикстуру)
    print(f"[FIXTURE] Удаляем проект {pid}...")
    del_resp = requests.delete(
        f"{base_url}/api-v2/projects/{pid}",
        headers=my_headers
    )
    if del_resp.ok:
        print(f"[FIXTURE] Проект {pid} успешно удалён.")
    else:
        print(f"[FIXTURE] Не удалось удалить проект {pid}. Статус: {
                del_resp.status_code}, ответ: {del_resp.text}")
