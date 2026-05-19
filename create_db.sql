-- Создать схему/таблицы
CREATE TABLE IF NOT EXISTS companies (
    id SERIAL PRIMARY KEY,
    hh_id BIGINT UNIQUE,
    name TEXT NOT NULL,
    url TEXT,
    area TEXT,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS vacancies (
    id SERIAL PRIMARY KEY,
    hh_id BIGINT UNIQUE,
    company_id INTEGER REFERENCES companies(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    url TEXT,
    salary_from NUMERIC,
    salary_to NUMERIC,
    currency TEXT,
    published_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT now()
);
