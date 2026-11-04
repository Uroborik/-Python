import json
import sqlite3


def create_tables(json_path, db_path="app.db"):
    with open(json_path, encoding="utf-8") as f:
        tables = json.load(f)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for name, fields in tables.items():
        columns = ", ".join(f"{field} {ftype}" for field, ftype in fields.items())
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} ({columns})")
    conn.commit()
    conn.close()


schema = {
    "authors": {"id": "INTEGER PRIMARY KEY", "name": "TEXT"},
    "books": {"id": "INTEGER PRIMARY KEY", "title": "TEXT", "year": "INTEGER"},
}
with open("schema.json", "w", encoding="utf-8") as f:
    json.dump(schema, f, ensure_ascii=False)

create_tables("schema.json")

conn = sqlite3.connect("app.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Созданные таблицы:", [row[0] for row in cursor.fetchall()])
conn.close()
