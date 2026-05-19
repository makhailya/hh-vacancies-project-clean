# Проект: Вакансии с hh.ru + PostgreSQL

Проект загружает вакансии из API hh.ru, сохраняет в PostgreSQL и предоставляет удобный интерфейс для поиска и анализа.

---

## 🚀 Возможности

- Загрузка данных о 10 компаниях с hh.ru  
- Сохранение вакансий в PostgreSQL  
- Просмотр компаний и количества их вакансий  
- Поиск вакансий по ключевым словам  
- Поиск вакансий с зарплатой выше средней  
- CLI-интерфейс  
- Тесты (pytest)  
- Структурированный код: API → Модели → Хранилище → БД → CLI  

---

## 📦 Используемые технологии

- Python 3.11+
- PostgreSQL 13+
- requests  
- psycopg2  
- poetry  
- pytest  

---

## 📁 Структура проекта
project/
├─ src/
│  ├─ hh_api.py
│  ├─ vacancy.py
│  ├─ storage.py
│  ├─ db_manager.py
│  ├─ load_data.py
│  └─ main.py
├─ tests/
├─ README.md
└─ pyproject.toml

---

## 🔧 Установка

```bash
git clone <repo>
cd project
poetry install

Создайте .env:

DATABASE_URL=postgresql://user:pass@localhost:5432/hh_db

▶️ Запуск

poetry run python src/main.py

🧪 Тестирование

poetry run pytest -v