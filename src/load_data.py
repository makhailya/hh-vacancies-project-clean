# src/load_data.py
from src.db_manager import DBManager
from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy

COMPANIES = [
    1740,  # Яндекс
    3529,  # Тинькофф
    78638,  # VK
    39305,  # Ozon
    3776,  # МТС
    2180,  # Альфа-Банк
    87021,  # Сбер
    15478,  # Wildberries
    1455,  # Рутуб
    588,  # Лаборатория Касперского
]


def load_companies_and_vacancies():
    hh = HeadHunterAPI()
    db = DBManager()

    print("Загружаем компании...")

    with db.conn.cursor() as cur:
        for company_id in COMPANIES:
            cur.execute(
                """
                INSERT INTO companies (hh_id, name)
                VALUES (%s, %s)
                ON CONFLICT (hh_id) DO NOTHING;
            """,
                (company_id, f"Компания {company_id}"),
            )

    print("Загружаем вакансии...")

    for company_id in COMPANIES:
        items = hh.get_vacancies(f"company_id:{company_id}")
        vacancies = [Vacancy.from_hh_item(i) for i in items]

        for v in vacancies:
            with db.conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO vacancies (hh_id, company_id, title, url,
                     salary_from, salary_to, currency)
                    SELECT %s, c.id, %s, %s, %s, %s, %s
                    FROM companies c
                    WHERE c.hh_id = %s
                    ON CONFLICT (hh_id) DO NOTHING;
                """,
                    (
                        v.hh_id,
                        v.title,
                        v.url,
                        v.salary_from,
                        v.salary_to,
                        v.currency,
                        v.company_hh_id,
                    ),
                )

    print("Готово!")
