import allure
import pytest


@pytest.mark.api
def test_status_code(api_client):
    response = api_client.get(url=api_client.base_url)
    assert response.status_code == 200
    assert response.status_code not in (300, 400, 500)
