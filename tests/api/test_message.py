import allure
import pytest
from data_schema.message_schema import schema
from jsonschema import validate
from fixtures.Create_json_for_message import json_message


@pytest.mark.api
def test_schema_message(api_client):
    response = api_client.get(url=api_client.base_url)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


@pytest.mark.api
def test_message_count(api_client):
    response = api_client.get(url=api_client.base_url + "count")
    assert response.status_code == 200


@pytest.mark.api
def test_post_message(api_client):
    response = api_client.post(url=api_client.base_url, json=json_message())
    assert response.status_code == 201