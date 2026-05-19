# src/storage.py
import os
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


class JSONSaver:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump([], f)

    def add_vacancies(self, vacancies: list):
        existing = self.get_vacancies()

        existing_ids = {v["hh_id"] for v in existing}
        new_unique = [v for v in vacancies if v["hh_id"] not in existing_ids]

        all_data = existing + new_unique

        with open(self.filename, "w") as f:
            json.dump(all_data, f, indent=2)

    def get_vacancies(self):
        with open(self.filename) as f:
            return json.load(f)

    def delete_vacancy(self, hh_id: int):
        data = self.get_vacancies()
        filtered = [v for v in data if v["hh_id"] != hh_id]

        with open(self.filename, "w") as f:
            json.dump(filtered, f, indent=2)
