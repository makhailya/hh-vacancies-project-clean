from database.create_db import create_database
from database.init_tables import create_tables
from database.db_manager import DBManager
import psycopg2


DB_NAME = "hh_project"
USER = "postgres"
PASSWORD = "12345"


def main():
    # Создаём базу
    create_database(DB_NAME, USER, PASSWORD)

    # Подключаемся
    conn = psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD)

    # Создаём таблицы
    create_tables(conn)
    print("Таблицы созданы.")

    # Пример использования DBManager
    db = DBManager(DB_NAME, USER, PASSWORD)

    print(db.get_companies_and_vacancies_count())


if __name__ == "__main__":
    main()
