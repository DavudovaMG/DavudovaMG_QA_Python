from sqlalchemy import create_engine
from sqlalchemy.sql import text


class SubjectTable:
    __scripts = {
     "delete_by_title": text(
          "DELETE FROM subject WHERE subject_title = :title_to_delete"),
     "insert_new": text(
         "INSERT INTO subject(\"subject_title\") VALUES (:new_name)"),
     "get_max_id": text(
         "SELECT MAX(\"subject_id\") FROM subject"),
     "get_all": text(
             "SELECT subject_id, subject_title FROM subject"),
     "update_subject_id": text(
         "UPDATE subject SET subject_title = :update_name WHERE "
         "subject_id = :id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subject(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_all"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def delete(self, name):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["delete_by_title"],
            {"title_to_delete": name}
        )
        conn.commit()
        conn.close()

    def create(self, name):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["insert_new"],
            {"new_name": name}
        )
        conn.commit()
        conn.close()

    def update_subject(self, new_update_name, max_id):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["update_subject_id"],
            {"update_name": new_update_name, "id": max_id}
        )
        conn.commit()
        conn.close()

    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()
        conn.close()
        return max_id
