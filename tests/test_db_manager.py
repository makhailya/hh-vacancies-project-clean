import psycopg2
from database.db_manager import DBManager
from database.init_tables import create_tables


def setup_database():
    conn = psycopg2.connect(dbname="hh_project", user="postgres", password="12345")
    create_tables(conn)

    with conn.cursor() as cur:
        cur.execute("DELETE FROM vacancies;")
        cur.execute("DELETE FROM companies;")

        cur.execute("INSERT INTO companies (hh_id, name) VALUES (1, 'TestCo');")
        cur.execute("""
            INSERT INTO vacancies (company_id, name, salary_from, salary_to, url)
            VALUES (1, 'Python Developer', 100000, 150000, 'https://example.com')
        """)

        conn.commit()
    conn.close()


def test_get_companies_and_vacancies_count():
    setup_database()
    db = DBManager("hh_project", "postgres", "12345")
    result = db.get_companies_and_vacancies_count()
    assert result[0][1] == 1


def test_get_vacancies_with_keyword():
    setup_database()
    db = DBManager("hh_project", "postgres", "12345")
    result = db.get_vacancies_with_keyword("python")
    assert len(result) == 1
