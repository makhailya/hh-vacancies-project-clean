import requests
from unittest.mock import patch, MagicMock
from src.hh_api import HeadHunterAPI


def test_get_vacancies_success():
    api = HeadHunterAPI()

    fake_json = {"items": [{"id": "1", "name": "Dev"}]}

    with patch("requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = fake_json
        mock_get.return_value = mock_resp

        data = api.get_vacancies("python")

        assert "items" in data
        assert data["items"][0]["name"] == "Dev"


def test_get_vacancies_fail():
    api = HeadHunterAPI()

    with patch("requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_get.return_value = mock_resp

        data = api.get_vacancies("python")

        assert data == {"items": []}
