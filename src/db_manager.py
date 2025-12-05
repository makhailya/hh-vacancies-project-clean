# src/db_manager.py
import os
from typing import List, Optional, Tuple

import psycopg2
import psycopg2.extras


class DBManager:
    """Класс для работы с БД PostgreSQL."""

    def __init__(self, dsn: Optional[str] = None):
        # DSN можно передавать из env (postgresql://user:pass@host:port/dbname)
        self.dsn = dsn or os.getenv("DATABASE_URL")
        self.conn = psycopg2.connect(self.dsn)
        self.conn.autocommit = True

    def close(self):
        self.conn.close()

    def get_companies_and_vacancies_count(self) -> List[Tuple[str, int]]:
        """Возвращает (company_name, vacancies_count)."""
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT c.name, COUNT(v.id) AS cnt
                FROM companies c
                LEFT JOIN vacancies v ON v.company_id = c.id
                GROUP BY c.id, c.name
                ORDER BY cnt DESC;
                """
            )
            return cur.fetchall()

    def get_all_vacancies(
        self,
    ) -> List[Tuple[str, str, Optional[float], Optional[float], str]]:
        """Возвращает список: (company_name, title,
        salary_from, salary_to, url)."""
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT c.name, v.title, v.salary_from, v.salary_to, v.url
                FROM vacancies v
                LEFT JOIN companies c ON v.company_id = c.id;
                """
            )
            return cur.fetchall()

    def get_avg_salary(self) -> Optional[float]:
        with self.conn.cursor() as cur:
            query = (
                "SELECT AVG((COALESCE(salary_from, 0) "
                "+ COALESCE(salary_to, 0)) / "
                "NULLIF((CASE WHEN salary_from IS NULL THEN 0 ELSE 1 END + "
                "CASE WHEN salary_to IS NULL THEN 0 ELSE 1 END), 0)) "
                "FROM vacancies;"
            )
            cur.execute(query)
            result = cur.fetchone()
            return result[0] if result else None

    def get_vacancies_with_higher_salary(self) -> List[Tuple]:
        avg = self.get_avg_salary() or 0
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT c.name, v.title, v.salary_from, v.salary_to, v.url
                FROM vacancies v
                JOIN companies c ON v.company_id = c.id
                WHERE (COALESCE((v.salary_from + v.salary_to) / 2.0, 0)) > %s;
                """,
                (avg,),
            )
            return cur.fetchall()

    def get_vacancies_with_keyword(self, keyword: str) -> List[Tuple]:
        pattern = f"%{keyword.lower()}%"
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT c.name, v.title, v.salary_from, v.salary_to, v.url
                FROM vacancies v
                JOIN companies c ON v.company_id = c.id
                WHERE LOWER(v.title) LIKE %s OR LOWER(v.description) LIKE %s;
                """,
                (pattern, pattern),
            )
            return cur.fetchall()
