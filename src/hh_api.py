import requests
from typing import List, Dict, Any, Optional


class HeadHunterAPI:
    URL = "https://api.hh.ru/vacancies"

    def __init__(self, per_page: int = 10):
        self.per_page = per_page

    def get_vacancies(self, text: str) -> Dict[str, Any]:
        """
        Возвращает словарь {"items": [...]}, даже если API вернул ошибку.
        Тесты ожидают строго такой формат.
        """
        params = {"text": text, "per_page": self.per_page}

        resp = requests.get(self.URL, params=params)

        if resp.status_code != 200:
            return {"items": []}

        data = resp.json()

        # Если API вернул словарь с ключом items → отлично
        if isinstance(data, dict) and "items" in data:
            return data

        # Если API вернул список → упаковываем
        if isinstance(data, list):
            return {"items": data}

        return {"items": []}
