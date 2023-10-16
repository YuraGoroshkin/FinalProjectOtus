import allure
import pytest
from data_schema.room_schema import schema
from jsonschema import validate
from fixtures.Api_auth import api_auth
from fixtures.Create_json_for_api import CreateJson

port = f":3001"


@allure.feature("Api")
@pytest.mark.api
def test_schema_room(api_client, request):
    base_url = f"{request.config.getoption('--url')}{port}/room/"
    response = api_client.get(url=base_url)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


@allure.feature("Api")
@pytest.mark.api
def test_add_room(api_client, request):
    url = request.config.getoption('--url')
    api_auth(api_client, url)
    base_url = f"{url}{port}/room/"
    response = api_client.post(url=base_url, json=CreateJson().json_room())
    assert response.status_code == 201


@allure.feature("Api")
@pytest.mark.parametrize('status, roomname', [(201, "simple"), (400, 100), (400, ""), (400, " "), (400, None)])
@pytest.mark.api
def test_add_room(api_client, request, roomname, status):
    url = request.config.getoption('--url')
    api_auth(api_client, url)
    base_url = f"{url}{port}/room/"
    response = api_client.post(url=base_url, json=CreateJson().json_room(roomname=roomname))
    assert response.status_code == status


@allure.feature("Api")
@pytest.mark.api
def test_add_room(api_client, request):
    url = request.config.getoption('--url')
    api_auth(api_client, url)
    base_url = f"{url}{port}/room/"
    old_count_room = len(api_client.get(url=base_url).json()['rooms'])
    api_client.post(url=base_url, json=CreateJson().json_room())
    new_count_room = len(api_client.get(url=base_url).json()['rooms'])
    assert old_count_room + 1 == new_count_room


@allure.feature("Api")
@pytest.mark.api
def test_add_room_no_auth(api_client, request):
    url = request.config.getoption('--url')
    base_url = f"{url}{port}/room/"
    response = api_client.post(url=base_url, json=CreateJson().json_room())
    assert response.status_code == 403


@allure.feature("Api")
@pytest.mark.parametrize('status, id', [(200, 1), (500, 200)])
@pytest.mark.api
def test_status_room_id_get(api_client, request, status, id):
    base_url = f"{request.config.getoption('--url')}{port}/room/{id}"
    response = api_client.get(url=base_url)
    assert response.status_code == status


@allure.feature("Api")
@pytest.mark.api
def test_status_room_id_put(api_client, request):
    url = request.config.getoption('--url')
    api_auth(api_client, url)
    base_url = f"{request.config.getoption('--url')}{port}/room/1"
    response = api_client.put(url=base_url, json=CreateJson().json_room())
    assert response.status_code == 202


@allure.feature("Api")
@pytest.mark.api
def test_status_room_id_delete(api_client, request):
    url = request.config.getoption('--url')
    api_auth(api_client, url)
    base_url = f"{url}{port}/room/"
    id_room = api_client.get(url=base_url).json()['rooms']
    if len(id_room) == 0:
        api_client.post(url=base_url, json=CreateJson().json_room())
        id_room = api_client.get(url=base_url).json()['rooms']
    response = api_client.delete(url=f"{request.config.getoption('--url')}{port}/room/{id_room[0]['roomid']}")
    assert response.status_code == 202


@allure.feature("Api")
@pytest.mark.api
def test_delete_room(api_client, request):
    url = request.config.getoption('--url')
    api_auth(api_client, url)
    base_url = f"{url}{port}/room/"
    old_count_room = api_client.get(url=base_url).json()
    if old_count_room == 0:
        api_client.post(url=base_url, json=CreateJson().json_room())
        old_count_room = api_client.get(url=base_url).json()
    id_room = old_count_room['rooms'][0]['roomid']
    api_client.delete(url=f"{request.config.getoption('--url')}{port}/room/{id_room}")
    new_count_room = len(api_client.get(url=base_url).json()['rooms'])
    assert len(old_count_room['rooms']) - 1 == new_count_room
