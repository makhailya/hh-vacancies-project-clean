# src/vacancy.py
from dataclasses import dataclass
from typing import Optional


@dataclass
class Vacancy:
    hh_id: int
    company_hh_id: Optional[int]
    title: str
    url: str
    salary_from: Optional[float] = None
    salary_to: Optional[float] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    published_at: Optional[str] = None


    def avg_salary(self) -> Optional[float]:
        """Средняя зарплата вакансии или None если отсутствуют данные."""
        if self.salary_from is None and self.salary_to is None:
            return None
        if self.salary_from is None:
            return float(self.salary_to)
        if self.salary_to is None:
            return float(self.salary_from)
        return float((self.salary_from + self.salary_to) / 2.0)

    # сравнение по средней зарплате
    def __lt__(self, other: "Vacancy") -> bool:
        return (self.avg_salary() or 0) < (other.avg_salary() or 0)

    def __repr__(self) -> str:
        return f"Vacancy(title={self.title!r}, avg_salary={self.avg_salary()})"

    @classmethod
    def from_hh_item(cls, item: dict) -> "Vacancy":
        """Создаёт Vacancy из структуры item API hh.ru."""
        hh_id = int(item.get("id"))
        company = item.get("employer") or {}
        company_hh_id = company.get("id")
        title = item.get("name")
        url = item.get("apply_alternate_url") or item.get("alternate_url")
        salary = item.get("salary")  # может быть None
        if salary:
            salary_from = salary.get("from")
            salary_to = salary.get("to")
            currency = salary.get("currency")
        else:
            salary_from = salary_to = currency = None
        description = item.get("snippet", {}).get("requirement") or item.get(
            "snippet", {}
        ).get("responsibility")
        published_at = item.get("published_at")
        return cls(
            hh_id=hh_id,
            company_hh_id=int(company_hh_id) if company_hh_id else None,
            title=title,
            url=url,
            salary_from=salary_from,
            salary_to=salary_to,
            currency=currency,
            description=description,
            published_at=published_at,
        )
