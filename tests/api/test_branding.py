import allure
import pytest
from data_schema.branding_schema import schema
from jsonschema import validate

port = f":3002"


@allure.feature("Api")
@pytest.mark.api
def test_status_branding(api_client, request):
    base_url = f"{request.config.getoption('--url')}{port}/branding/"
    response = api_client.get(url=base_url)
    assert response.status_code == 200


@allure.feature("Api")
@pytest.mark.api
def test_schema_branding(api_client, request):
    base_url = f"{request.config.getoption('--url')}{port}/branding/"
    response = api_client.get(url=base_url)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)
