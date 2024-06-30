import sqlite3

def create_tables():
    # Підключення до бази даних (створення, якщо не існує)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Створення таблиці 'websites'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS websites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            status TEXT NOT NULL,
            checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Збереження змін та закриття підключення
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    print("Таблиці створено успішно")
