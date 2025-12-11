from unittest.mock import MagicMock, patch
from src.db_manager import DBManager


def fake_cursor(rows):
    m = MagicMock()
    m.__enter__.return_value = m
    m.fetchall.return_value = rows
    return m


def test_get_companies_and_vacancies_count():
    rows = [("Company A", 5), ("Company B", 3)]

    with patch("psycopg2.connect") as mock_conn:
        conn = MagicMock()
        conn.cursor.return_value = fake_cursor(rows)
        mock_conn.return_value = conn

        db = DBManager()
        result = db.get_companies_and_vacancies_count()

        assert len(result) == 2
        assert result[0] == ("Company A", 5)


def test_get_vacancies_with_keyword():
    rows = [("Company", "Python Dev", 100, "url")]

    with patch("psycopg2.connect") as mock_conn:
        conn = MagicMock()
        conn.cursor.return_value = fake_cursor(rows)
        mock_conn.return_value = conn

        db = DBManager()
        result = db.get_vacancies_with_keyword("python")

        assert len(result) == 1
        assert "Python" in result[0][1]
