from src.storage import JSONSaver
import json


def test_json_saver_add_and_get(tmp_path):
    file = tmp_path / "test.json"
    saver = JSONSaver(str(file))

    saver.add_vacancies([{"hh_id": 1, "title": "Dev"}])
    saver.add_vacancies([{"hh_id": 1, "title": "Dev"}])  # дубль
    saver.add_vacancies([{"hh_id": 2, "title": "Python"}])

    data = saver.get_vacancies()

    assert len(data) == 2
    assert {v["hh_id"] for v in data} == {1, 2}


def test_json_saver_delete(tmp_path):
    file = tmp_path / "test.json"
    saver = JSONSaver(str(file))

    saver.add_vacancies([{"hh_id": 1, "title": "Dev"}])
    saver.add_vacancies([{"hh_id": 2, "title": "Python"}])

    saver.delete_vacancy(1)
    data = saver.get_vacancies()

    assert len(data) == 1
    assert data[0]["hh_id"] == 2
