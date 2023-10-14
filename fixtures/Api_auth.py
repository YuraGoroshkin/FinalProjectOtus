import allure


@allure.step('Авторизация -> cookie')
def api_auth(session, url, username="admin", password="password"):
    path_auth = ":3004/auth/login"
    data = {"username": username, "password": password}
    return session.post(url=f"{url}{path_auth}", json=data)
