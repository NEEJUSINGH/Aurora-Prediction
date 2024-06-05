import sqlite3

def create_database():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    value TEXT
                )''')
    conn.commit()
    conn.close()

def insert_data(data):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    for item in data:
        c.execute("INSERT INTO data (name, value) VALUES (?, ?)", (item['name'], item['value']))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()

