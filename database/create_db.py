import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_database(db_name: str, user: str, password: str, host: str = "localhost") -> None:
    """
    Создаёт базу данных, если она не существует.
    """
    conn = psycopg2.connect(dbname="postgres", user=user, password=password, host=host)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';")
    exists = cur.fetchone()

    if not exists:
        cur.execute(f"CREATE DATABASE {db_name};")
        print(f"База данных {db_name} создана.")
    else:
        print(f"База данных {db_name} уже существует.")

    cur.close()
    conn.close()
    