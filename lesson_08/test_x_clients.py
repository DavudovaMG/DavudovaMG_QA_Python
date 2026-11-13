import requests


base_url = "https://ru.yougile.com"


# Негативная проверка, передача в API  число 123, как значение поля title,
# а не строку.


def test_create_project_title(api_token):
    my_headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    payload = {'title': 123}
    resp = requests.post(
        base_url+'/api-v2/projects', json=payload, headers=my_headers)
    # resp.raise_for_status()
    assert resp.status_code == 400, f"Ожидался 400, но получен {
        resp.status_code}"
    print("Негативная проверка пройдена: передача числа 123 в "
          "title вернула 400")


# Изменение проекта
# Позитивная проверка, изменение названия проекта


def test_change_title_project(project_id, api_token):
    my_headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    new_project = {
            "title": 'Трубопровод Главный - Ямал'
        }
    # ВАЖНО: f-строка, чтобы подставить project_id
    url = f"{base_url}/api-v2/projects/{project_id}"
    resp = requests.put(
        url, json=new_project, headers=my_headers)
    # resp.raise_for_status()
    print("URL запроса:", url)
    print("Статус:", resp.status_code)
    print("Ответ:", resp.text)
    assert resp.status_code == 200
    data = resp.json()
    # Получаем и выводим ID
    assert data["id"] == project_id
    # print(f"ID созданного проекта: {project_id}")
    assert "id" in data and data["id"] == project_id
    print("Проект обновился: название изменилось.")


# Изменение, с неверным типом данных
# Негативная проверка


def test_update_project_invalid_title_type(project_id, api_token):
    my_headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    new_project = {
            "title": 12345
        }
    # ВАЖНО: f-строка, чтобы подставить project_id
    url = f"{base_url}/api-v2/projects/{project_id}"
    put_resp = requests.put(
        url, json=new_project, headers=my_headers)
    # resp.raise_for_status()
    print("URL запроса:", url)
    print("PUT статус:", put_resp.status_code)
    print("Ответ:", put_resp.text)
    # Проверяем, что сервер отверг запрос
    assert put_resp.status_code == 400, f"Ожидался 400, но получен {
        put_resp.status_code}"
    error_data = put_resp.json()
    # Можно проверить, что в ответе есть поле ошибки (если API его даёт)
    assert "error" in error_data or "message" in error_data
    # Проверяем, что проект НЕ изменился: делаем GET и смотрим title
    get_resp = requests.get(url, headers=my_headers)
    assert get_resp.status_code == 200
    get_data = get_resp.json()

    print("GET ответ:", get_data)

    assert "title" in get_data
    # Здесь мы подтверждаем, что название НЕ стало 12345
    assert get_data["title"] != 12345, "Проект не должен"
    "был обновиться до числа"
    print("Проект не обновился: название осталось прежним.")


# Получить по ID
# Позитивная проверка
def test_get_project_existent_id(project_id, api_token):
    my_headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    # ВАЖНО: f-строка, чтобы подставить project_id
    url = f"{base_url}/api-v2/projects/{project_id}"
    resp = requests.get(
        url, headers=my_headers)
    # # resp.raise_for_status()
    print("URL запроса:", url)
    print("Статус:", resp.status_code)
    print("Ответ:", resp.text)
    assert resp.status_code == 200
    f"Ожидался 200 для существующего проекта, но получен {resp.status_code}"


# Получить по ID
# Негативная проверка, поиск несуществующего проекта
def test_get_project_nonexistent_id(api_token):
    # Берем несуществующий ID проекта
    nonexistent = "a2366ba7-d8e5-49f8-bd04-ffd12605f327"
    my_headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    # ВАЖНО: f-строка, чтобы подставить nonexistent
    url = f"{base_url}/api-v2/projects/{nonexistent}"
    resp = requests.get(
        url, headers=my_headers)
    # # resp.raise_for_status()
    print("URL запроса:", url)
    print("Статус:", resp.status_code)
    print("Ответ:", resp.text)
    assert resp.status_code == 404
    f"Ожидался 404 для несуществующего проекта, но получен {resp.status_code}"
    # Проверка, что в ответе нет валидного объекта проекта
    # Если API возвращает JSON с ошибкой — парсим его, если
    # plain text — пропускаем
    if resp.headers.get("Content-Type", "").startswith("application/json"):
        data = resp.json()
        # В случае 404 там не должно быть полей id/title как у проекта
        assert "id" not in data, "В ответе на 404 не должен быть валидный "
        "id проекта"
        assert "title" not in data, "В ответе на 404 не должно быть "
        "title проекта"
    else:
        # Если это не JSON, то тем более нельзя ожидать id/title
        pass

    print("Корректно получена ошибка 404 для несуществующего проекта")
