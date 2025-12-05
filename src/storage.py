# src/storage.py
import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List


class BaseSaver(ABC):
    @abstractmethod
    def add_vacancies(self, vacancies: List[Dict[str, Any]]) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_vacancies(self) -> List[Dict[str, Any]]:
        raise NotImplementedError


class JSONSaver(BaseSaver):
    def __init__(self, filename: str = "vacancies.json"):
        self._path = Path(filename)
        if not self._path.exists():
            self._path.write_text("[]", encoding="utf-8")

    def add_vacancies(self, vacancies: List[Dict[str, Any]]) -> None:
        data = self.get_vacancies()
        # убрать дубли по hh_id
        existing_ids = {v.get("hh_id") for v in data if v.get("hh_id")}
        for v in vacancies:
            if v.get("hh_id") not in existing_ids:
                data.append(v)
        self._path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def get_vacancies(self) -> List[Dict[str, Any]]:
        return json.loads(self._path.read_text(encoding="utf-8"))
