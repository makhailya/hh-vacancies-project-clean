# src/cli.py
from src.db_manager import DBManager


def main():
    db = DBManager()
    try:
        while True:
            print("1. Список компаний и кол-во вакансий")
            print("2. Все вакансии")
            print("3. Средняя зарплата")
            print("4. Вакансии с зарплатой выше средней")
            print("5. Поиск по ключевому слову")
            print("0. Выход")
            cmd = input("Выберите пункт: ").strip()
            if cmd == "1":
                for name, cnt in db.get_companies_and_vacancies_count():
                    print(f"{name}: {cnt}")
            elif cmd == "2":
                for row in db.get_all_vacancies():
                    print(row)
            elif cmd == "3":
                print("Avg salary:", db.get_avg_salary())
            elif cmd == "4":
                for r in db.get_vacancies_with_higher_salary():
                    print(r)
            elif cmd == "5":
                kw = input("Введите ключевое слово: ").strip()
                for r in db.get_vacancies_with_keyword(kw):
                    print(r)
            elif cmd == "0":
                break
    finally:
        db.close()


if __name__ == "__main__":
    main()
