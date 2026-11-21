from SubjectTable import SubjectTable

db = SubjectTable(
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase")


def test_get_one_subject():
    name = "QA"
    # Удаление старых дублей
    db.delete(name)
    # Считаем, сколько записей было ДО
    initial_rows = db.get_subject()
    initial_count = len(initial_rows)
    # Добавляем предмет
    db.create(name)
    # Считаем, сколько записей стало ПОСЛЕ
    final_rows = db.get_subject()
    final_count = len(final_rows)
    # Проверяем, что среди строк есть ровно одна с name = "QA"
    qa_rows = [r for r in final_rows if r["subject_title"] == name]
    # Удаляем добавленный предмет
    db.delete(name)
    assert final_count == initial_count + 1, (
        f"Количество записей не увеличилось на 1: было {initial_count}, стало {
            final_count}")
    assert len(qa_rows) == 1, (f"Найдено больше одной записи с названием '{
        name}'; найдено {len(qa_rows)}")


def test_update_one_subject():
    name = "QA"
    # Удаление старых дублей
    db.delete(name)
    # Добавляем предмет
    db.create(name)
    # В переменной сохраняем MAX ID
    max_id = db.get_max_id()
    # Вносим изменения в наименование
    update_name = "QA engineer"
    db.update_subject(update_name, max_id)
    # Читаем данные из БД, чтобы проверить реальное состояние
    rows = db.get_subject()
    # Находим строку с нужным ID
    updated_row = next((r for r in rows if r["subject_id"] == max_id), None)
    db.delete(update_name)
    # Проверяем, что название действительно изменилось
    assert updated_row["subject_title"] == update_name, (
        f"Название не обновилось: ожидалось '{update_name}', "
        f"а в базе осталось '{updated_row['subject_title']}'"
    )


def test_delete_one_subject():
    name = "QA"
    # Удаление старых дублей
    db.delete(name)
    # Считаем, сколько записей было ДО
    initial_rows = db.get_subject()
    initial_count = len(initial_rows)
    # Добавляем предмет
    db.create(name)
    # Проверяем, что среди строк есть ровно одна с name = "QA"
    rows_after_create = db.get_subject()
    qa_rows_after_create = [r for r in rows_after_create if r[
        "subject_title"] == name]
    assert len(qa_rows_after_create) == 1, (
     f"Ожидается ровно 1 запись с названием '{name}', "
     f"найдено {len(qa_rows_after_create)}")
    # Удаляем добавленный предмет
    db.delete(name)
    # Считаем, сколько записей стало ПОСЛЕ
    final_rows = db.get_subject()
    final_count = len(final_rows)
    assert initial_count == final_count, (
        f"Количество записей не увеличилось на 1: было {initial_count}, стало {
            final_count}")
