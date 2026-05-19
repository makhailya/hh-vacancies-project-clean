# src/vacancy.py
from dataclasses import dataclass
from typing import Optional


@dataclass
class Vacancy:
    hh_id: int
    company_hh_id: Optional[int]
    title: str
    url: str
    salary_from: Optional[float] = 0
    salary_to: Optional[float] = 0
    currency: Optional[str] = None
    description: Optional[str] = None
    published_at: Optional[str] = None


    def avg_salary(self):
        if self.salary_from and self.salary_to:
            return (self.salary_from + self.salary_to) // 2
        if self.salary_from:
            return self.salary_from
        if self.salary_to:
            return self.salary_to
        return 0

    # сравнение по средней зарплате
    def __lt__(self, other: "Vacancy") -> bool:
        return (self.avg_salary() or 0) < (other.avg_salary() or 0)

    def __repr__(self) -> str:
        return f"Vacancy(title={self.title!r}, avg_salary={self.avg_salary()})"

    @classmethod
    def from_hh_item(cls, item: dict):
        salary = item.get("salary") or {}

        salary_from = salary.get("from") or 0
        salary_to = salary.get("to") or 0

        return cls(
            hh_id=int(item["id"]),
            company_hh_id=int(item["employer"]["id"]),
            title=item["name"],
            url=item["alternate_url"],
            salary_from=salary_from,
            salary_to=salary_to,
        )
