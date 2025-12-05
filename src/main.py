# src/main.py
from src.cli import main as cli_main
from src.load_data import load_companies_and_vacancies


def main():
    load_data = input("Загрузить данные с hh? (y/n): ").strip().lower()
    if load_data == "y":
        load_companies_and_vacancies()

    cli_main()


if __name__ == "__main__":
    main()
