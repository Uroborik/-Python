import sqlite3


class User:
    id: int
    name: str
    age: int


class ORMMapper:
    types = {int: "INTEGER", str: "TEXT", float: "REAL"}

    def __init__(self, model):
        self.model = model

    def convert_to_db(self, db_path="orm.db"):
        name = self.model.__name__.lower()
        fields = self.model.__annotations__
        columns = ", ".join(f"{field} {self.types[ftype]}" for field, ftype in fields.items())
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} ({columns})")
        conn.commit()
        conn.close()
        return name


mapper = ORMMapper(User)
table = mapper.convert_to_db()

conn = sqlite3.connect("orm.db")
cursor = conn.cursor()
cursor.execute(f"PRAGMA table_info({table})")
print("Таблица:", table)
print("Поля:", [(row[1], row[2]) for row in cursor.fetchall()])
conn.close()
