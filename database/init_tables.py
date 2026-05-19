import psycopg2


def create_tables(conn):
    """
    Создаёт таблицы companies и vacancies.
    """

    create_companies = """
    CREATE TABLE IF NOT EXISTS companies (
        id SERIAL PRIMARY KEY,
        hh_id INTEGER UNIQUE NOT NULL,
        name VARCHAR(255) NOT NULL
    );
    """

    create_vacancies = """
    CREATE TABLE IF NOT EXISTS vacancies (
        id SERIAL PRIMARY KEY,
        company_id INTEGER REFERENCES companies(id) ON DELETE CASCADE,
        name VARCHAR(255) NOT NULL,
        salary_from INTEGER,
        salary_to INTEGER,
        url TEXT NOT NULL
    );
    """

    with conn.cursor() as cur:
        cur.execute(create_companies)
        cur.execute(create_vacancies)
        conn.commit()