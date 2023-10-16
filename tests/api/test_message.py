import allure
import pytest
from data_schema.message_schema import schema
from jsonschema import validate
from fixtures.Create_json_for_api import CreateJson
from fixtures.Api_auth import api_auth


@allure.feature("Api")
@pytest.mark.api
def test_schema_message(api_client):
    response = api_client.get(url=api_client.base_url)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


@allure.feature("Api")
@pytest.mark.api
def test_message_count(api_client):
    response = api_client.get(url=api_client.base_url + "count")
    assert response.status_code == 200


@allure.feature("Api")
@pytest.mark.api
def test_post_message(api_client):
    response = api_client.post(url=api_client.base_url, json=CreateJson().json_message())
    assert response.status_code == 201


@allure.feature("Api")
@pytest.mark.parametrize('status, name', [(201, "simple"), (400, 100), (400, ""), (400, " "), (400, None)])
@pytest.mark.api
def test_message_field_name(api_client, status, name):
    response = api_client.post(url=api_client.base_url, json=CreateJson().json_message(name=name))
    assert response.status_code == status


@allure.feature("Api")
@pytest.mark.parametrize('status, subject', [(201, "subject field"), (400, 100), (400, ""), (400, " "), (400, None)])
@pytest.mark.api
def test_message_field_name(api_client, status, subject):
    response = api_client.post(url=api_client.base_url, json=CreateJson().json_message(subject=subject))
    assert response.status_code == status


@allure.feature("Api")
@pytest.mark.api
def test_get_id_message(api_client):
    response_id = api_client.get(url=api_client.base_url).json()['messages'][0]['id']
    response = api_client.get(url=api_client.base_url + f"{response_id}")
    assert response.status_code == 200


@allure.feature("Api")
@pytest.mark.api
def test_get_id_message(api_client, request):
    response_id = api_client.get(url=api_client.base_url).json()['messages'][0]['id']
    url = request.config.getoption('--url')
    api_auth(api_client, url)
    response = api_client.delete(url=api_client.base_url + f"{response_id}")
    assert response.status_code == 202
