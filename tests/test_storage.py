from src.storage import JSONSaver


def test_json_saver(tmp_path):
    file = tmp_path / "test.json"
    saver = JSONSaver(str(file))

    saver.add_vacancies([{"hh_id": 1, "title": "Dev"}])
    saver.add_vacancies([{"hh_id": 1, "title": "Dev"}])  # дубль

    data = saver.get_vacancies()
    assert len(data) == 1
