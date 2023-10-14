from fixtures.pages.Home import HomePage
import pytest


# @pytest.mark.parametrize('description', [("there are 20 charact"), ("")])
@pytest.mark.ui
def test_send_valid_form(browser):
    HomePage.submit_form(browser, description="there are 20 charact", )
    data = HomePage.get_acces_submit_form(browser)
    print(data)
    assert "Thanks for getting in touch" in data

