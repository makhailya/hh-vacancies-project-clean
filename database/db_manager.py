import psycopg2


class DBManager:
    """
    Класс для работы с базой данных вакансий.
    """
    def __init__(self, db_name: str, user: str, password: str, host: str = "localhost"):
        self.conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host)

    def get_companies_and_vacancies_count(self):
        q = """
        SELECT c.name, COUNT(v.id)
        FROM companies c
        LEFT JOIN vacancies v ON c.id = v.company_id
        GROUP BY c.name;
        """
        with self.conn.cursor() as cur:
            cur.execute(q)
            return cur.fetchall()

    def get_all_vacancies(self):
        q = """
        SELECT c.name, v.name, v.salary_from, v.url
        FROM vacancies v
        JOIN companies c ON c.id = v.company_id;
        """
        with self.conn.cursor() as cur:
            cur.execute(q)
            return cur.fetchall()

    def get_avg_salary(self):
        q = """
        SELECT AVG((salary_from + salary_to) / 2.0)
        FROM vacancies
        WHERE salary_from IS NOT NULL AND salary_to IS NOT NULL;
        """
        with self.conn.cursor() as cur:
            cur.execute(q)
            return cur.fetchone()[0]

    def get_vacancies_with_higher_salary(self):
        q = """
        SELECT name, salary_from, salary_to
        FROM vacancies
        WHERE (salary_from + salary_to) / 2 > (
            SELECT AVG((salary_from + salary_to) / 2.0) FROM vacancies
        );
        """
        with self.conn.cursor() as cur:
            cur.execute(q)
            return cur.fetchall()

    def get_vacancies_with_keyword(self, keyword: str):
        q = """
        SELECT name, salary_from, salary_to, url
        FROM vacancies
        WHERE LOWER(name) LIKE LOWER(%s);
        """
        with self.conn.cursor() as cur:
            cur.execute(q, (f"%{keyword}%",))
            return cur.fetchall()
