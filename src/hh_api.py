# src/hh_api.py
import logging
from typing import Any, Dict, List, Optional

import requests

logger = logging.getLogger(__name__)


class HeadHunterAPI:
    """Клиент для получения вакансий с hh.ru через публичный API."""

    BASE_URL = "https://api.hh.ru"

    def __init__(self, per_page: int = 100):
        self.per_page = per_page

    def _get(
        self, path: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        url = f"{self.BASE_URL}{path}"
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        return resp.json()

    def get_vacancies(
        self, text: str, per_page: Optional[int] = None, pages: int = 1
    ) -> List[Dict[str, Any]]:
        """
        Получить вакансии по поисковому запросу `text`.
        Возвращает список словарей (как в API).
        """
        per_page = per_page or self.per_page
        results: List[Dict[str, Any]] = []
        for page in range(pages):
            params = {"text": text, "per_page": per_page, "page": page}
            data = self._get("/vacancies", params=params)
            items = data.get("items", [])
            logger.debug("Fetched %d items from page %d", len(items), page)
            results.extend(items)
            if len(items) < per_page:
                break
        return results
