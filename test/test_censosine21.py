import pytest
from censosine21 import CensosINE21

@pytest.fixture
def mock_api_response():
    return {
        "metadata": [{'row': 'ID_TENEN_VIV'}],
        "data": [{'SHOGARES': 13988628, 'ID_TENEN_VIV': 'En propiedad'},
                 {'SHOGARES': 2983617, 'ID_TENEN_VIV': 'En alquiler'},
                 {'SHOGARES': 1564368, 'ID_TENEN_VIV': 'Otro régimen de tenencia'},
                 {'SHOGARES': 2607, 'ID_TENEN_VIV': 'No consta'}]
    }


@pytest.fixture
def mock_requests_post(monkeypatch, mock_api_response):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    def mock_post(*args, **kwargs):
        return MockResponse(mock_api_response, 200)

    monkeypatch.setattr("requests.post", mock_post)


def test_post_method(mock_requests_post):
    censos = CensosINE21()
    response = censos.post("hog", 'SHOGARES', ['ID_TENEN_VIV'], "ES")
    assert response is not None
    assert censos.table == "hog"
    assert censos.metrics == 'SHOGARES'
    assert censos.variables == ['ID_TENEN_VIV']
    assert censos.language == 'ES'
    assert censos.metadata == [{'row': 'ID_TENEN_VIV'}]
    assert censos.data == [{'SHOGARES': 13988628, 'ID_TENEN_VIV': 'En propiedad'},
                      {'SHOGARES': 2983617, 'ID_TENEN_VIV': 'En alquiler'},
                      {'SHOGARES': 1564368, 'ID_TENEN_VIV': 'Otro régimen de tenencia'},
                      {'SHOGARES': 2607, 'ID_TENEN_VIV': 'No consta'}]


def test_to_csv_method(tmp_path):
    censos = CensosINE21()
    censos.data = [{"key1": "value1", "key2": "value2"}]
    file_path = tmp_path / "test.csv"
    censos.to_csv(file_path)
    assert file_path.exists()


def test_filter_method():
    censos = CensosINE21()
    censos.data = [
        {"key": "value1"},
        {"key": "value2"},
        {"key": "value1"}
    ]
    filtered_data = censos.filter("key", "value1")
    assert len(filtered_data) == 2
    assert all(item["key"] == "value1" for item in filtered_data)
