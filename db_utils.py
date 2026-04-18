import sqlite3

def create_database(db_name):
    connection = sqlite3.connect(db_name)
    print(f"Database '{db_name}' created successfully!")
    connection.close()


def create_table(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    """)

    connection.commit()
    print("Table 'users' created successfully!")
    connection.close()