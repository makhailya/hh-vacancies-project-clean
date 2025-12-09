import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Создаёт соединение с БД."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Соединение с БД {db_file} установлено.")
    except Error as e:
        print(f"Ошибка подключения к БД: {e}")
    return conn

def create_table(conn, create_table_sql):
    """Создаёт таблицу по SQL-запросу."""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Таблица создана.")
    except Error as e:
        print(f"Ошибка создания таблицы: {e}")

def setup_database():
    """Основная функция: создаёт БД и таблицы."""
    database = "vacancies.db"

    # SQL-запрос для таблицы организаций
    sql_create_organizations_table = """
    CREATE TABLE IF NOT EXISTS organizations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
    """

    # SQL-запрос для таблицы вакансий
    sql_create_vacancies_table = """
    CREATE TABLE IF NOT EXISTS vacancies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        salary TEXT,
        organization_id INTEGER,
        FOREIGN KEY (organization_id) REFERENCES organizations (id) ON DELETE CASCADE
    );
    """

    # Создаём соединение
    conn = create_connection(database)

    if conn is not None:
        # Создаём таблицы
        create_table(conn, sql_create_organizations_table)
        create_table(conn, sql_create_vacancies_table)

        # Закрываем соединение
        conn.close()
    else:
        print("Ошибка: не удалось установить соединение с БД.")

# Если нужно запустить вручную (для тестов)
if __name__ == "__main__":
    setup_database()
