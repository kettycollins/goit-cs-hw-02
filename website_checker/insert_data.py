import sqlite3
import requests
from datetime import datetime

# Список вебсайтів для перевірки
websites = ["https://google.com", "https://facebook.com", "https://twitter.com"]

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "UP"
        else:
            return "DOWN"
    except requests.RequestException:
        return "DOWN"

def insert_data():
    # Підключення до бази даних
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Перевірка кожного вебсайту та вставка результатів у таблицю
    for website in websites:
        status = check_website(website)
        cursor.execute('''
            INSERT INTO websites (url, status, checked_at)
            VALUES (?, ?, ?)
        ''', (website, status, datetime.now()))

    # Збереження змін та закриття підключення
    conn.commit()
    conn.close()

if __name__ == '__main__':
    insert_data()
    print("Дані успішно вставлено у таблиці")
