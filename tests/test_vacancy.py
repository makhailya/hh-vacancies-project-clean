from src.vacancy import Vacancy


def test_avg_salary():
    v = Vacancy(
        hh_id=1,
        company_hh_id=1,
        title="Dev",
        url="",
        salary_from=100,
        salary_to=200,
    )
    assert v.avg_salary() == 150


def test_from_hh_item():
    item = {
        "id": "123",
        "name": "Python Developer",
        "alternate_url": "http://example.com",
        "salary": {"from": 100, "to": 200, "currency": "RUR"},
        "employer": {"id": "10"},
    }
    v = Vacancy.from_hh_item(item)
    assert v.hh_id == 123
    assert v.company_hh_id == 10
    assert v.title == "Python Developer"
