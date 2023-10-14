import allure
import pytest
from data_schema.room_schema import schema
from jsonschema import validate
from fixtures.Api_auth import api_auth
from fixtures.Create_json_for_api import CreateJson

port = f":3001"


@pytest.mark.api
def test_schema_room(api_client, request):
    base_url = f"{request.config.getoption('--url')}{port}/room/"
    response = api_client.get(url=base_url)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


@pytest.mark.api
def test_add_room(api_client, request):
    url = request.config.getoption('--url')
    api_auth(api_client, url)
    base_url = f"{url}{port}/room/"
    response = api_client.post(url=base_url, json=CreateJson().json_room())
    assert response.status_code == 201


@pytest.mark.api
def test_add_room_no_auth(api_client, request):
    url = request.config.getoption('--url')
    base_url = f"{url}{port}/room/"
    response = api_client.post(url=base_url, json=CreateJson().json_room())
    assert response.status_code == 403


@pytest.mark.parametrize('status, id', [(200, 1), (500, 200)])
@pytest.mark.api
def test_status_room_id(api_client, request, status, id):
    base_url = f"{request.config.getoption('--url')}{port}/room/{id}"
    response = api_client.get(url=base_url)
    assert response.status_code == status
