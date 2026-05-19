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


def test_avg_salary_missing():
    v = Vacancy(
        hh_id=1,
        company_hh_id=1,
        title="Dev",
        url="",
        salary_from=None,
        salary_to=None,
    )
    assert v.avg_salary() == 0


def test_comparison():
    v1 = Vacancy(1, 1, "A", "", 100, 200)
    v2 = Vacancy(2, 2, "B", "", 300, 400)

    assert v2 > v1
    assert v1 < v2


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
    assert v.salary_from == 100
    assert v.salary_to == 200


def test_from_hh_item_no_salary():
    item = {
        "id": "123",
        "name": "Python Developer",
        "alternate_url": "http://example.com",
        "salary": None,
        "employer": {"id": "10"},
    }
    v = Vacancy.from_hh_item(item)
    assert v.salary_from == 0
    assert v.salary_to == 0
