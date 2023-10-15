from fixtures.pages.Home import HomePage
from faker import Faker
import pytest
import allure

fake = Faker()


@allure.description("Тест проверят отправление формы с валидными значениями description")
@allure.feature("Ui")
@pytest.mark.parametrize('characteristic, value',
                         [("20_characters", "there are 20 charact"),
                          ("2000_characters", str(fake.random_number(digits=2000)))], ids=["valid1", "valid2"])
@pytest.mark.ui
def test_send_valid_form_description(browser, characteristic, value):
    HomePage.submit_form(browser, description=value, )
    data = HomePage.get_acces_submit_form(browser)
    assert data is not None
    assert "Thanks for getting in touch" in data


@allure.description("Тест проверят отправление формы с НЕ валидными значениями description")
@allure.feature("Ui")
@pytest.mark.parametrize('characteristic, value',
                         [("less_than_19_characters", "there are 20 charac"), ("emptiness", ""),
                          ("more_than_2000", str(fake.random_number(digits=2001)))],
                         ids=["not_valid1", "not_valid2", "not_valid3"])
@pytest.mark.ui
def test_send_not_valid_form_description(browser, characteristic, value):
    HomePage.submit_form(browser, description=value, )
    data = HomePage.get_alert_submit_form(browser)
    assert data is not None
    assert "size must be between 20 and 2000" or "размер должен находиться в диапазоне от 20 до 2000" in data


@allure.description("Тест проверят отправление формы с валидными значениями subject")
@allure.feature("Ui")
@pytest.mark.parametrize('characteristic, value',
                         [("5_characters", "5 char"),
                          ("100_characters", str(fake.random_number(digits=100)))], ids=["valid1", "valid2"])
@pytest.mark.ui
def test_send_subject_form(browser, characteristic, value):
    HomePage.submit_form(browser, subject=value, )
    data = HomePage.get_acces_submit_form(browser)
    assert data is not None
    assert "Thanks for getting in touch" in data


@allure.description("Тест проверят отправление формы с НЕ валидными значениями subject")
@allure.feature("Ui")
@pytest.mark.parametrize('characteristic, value',
                         [("less_than_5_characters", str(fake.random_number(digits=3))), ("emptiness", ""),
                          ("more_than_100", str(fake.random_number(digits=101)))],
                         ids=["not_valid1", "not_valid2", "not_valid3"])
@pytest.mark.ui
def test_send_not_subject_form_description(browser, characteristic, value):
    HomePage.submit_form(browser, subject=value, )
    data = HomePage.get_alert_submit_form(browser)
    assert data is not None
    assert "size must be between 5 and 100" or "размер должен находиться в диапазоне от 5 до 100" in data
