-- Вибір всіх записів з таблиці 'websites'
SELECT * FROM websites;

-- Вибір усіх доступних вебсайтів (які є UP)
SELECT * FROM websites WHERE status = 'UP';

-- Вибір усіх недоступних вебсайтів (які є DOWN)
SELECT * FROM websites WHERE status = 'DOWN';

-- Вибір останніх перевірок кожного вебсайту
SELECT url, status, MAX(checked_at) as last_checked
FROM websites
GROUP BY url;
