#!/bin/bash

# Ім'я файлу логів
LOGFILE="website_status.log"

# Запуск скрипту для створення таблиць
python3 create_tables.py

# Запуск скрипту для перевірки вебсайтів та вставки даних
python3 insert_data.py

# Запис результатів у файл логів
echo "Результати перевірки вебсайтів:" > $LOGFILE
sqlite3 example.db "SELECT url, status FROM websites ORDER BY checked_at DESC;" >> $LOGFILE

# Вивід повідомлення про завершення роботи
echo "Результати записано у файл логів $LOGFILE"
