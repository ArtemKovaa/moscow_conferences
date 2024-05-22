import uuid
import db_module.utils.execute_query as db
from moscow_conferences.settings import BASE_DIR
from db_module.utils import setup_db

class ConferenceDao:

    def __init__(self):
        setup_db.init_schema(BASE_DIR)

    def get_all(self):
        result = db.execute_query("SELECT * FROM conferences")

        if result is Exception:
            raise result

        return [{"id": i[0], "name": i[1]} for i in result]

    def save(self, data):
        result = db.execute_query(
            "INSERT INTO conferences (id, name, description, start_date, location) VALUES (?, ?, ?, ?, ?)",
            (uuid.uuid4().__str__(), data['name'], data['description'], data['start_date'], data['location'])
        )
        if result is Exception:
            raise result

    def get_by_id(self, conference_id):
        result = db.execute_query("SELECT * FROM conferences WHERE id = ?", (conference_id.__str__(),))

        if result is Exception:
            raise result

        return result

    def update_record(self, id, record):
        result = db.execute_query(
            "UPDATE conferences SET name = ?, description = ?, start_date = ?, location = ? WHERE id = ?",
            (record['name'], record['description'], record['start_date'], record['location'], id.__str__())
        )

        if result is Exception:
            raise result

    def delete_by_id(self, conference_id):
        result = db.execute_query("DELETE FROM conferences WHERE id = ?", (conference_id.__str__(),))

        if result is Exception:
            raise result
