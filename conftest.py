import os
import logging
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import FirefoxOptions, ChromeOptions, EdgeOptions
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.by import By
import allure
import json
import requests

DRIVERS = os.path.expanduser


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")
    parser.addoption("--url", default="http://127.0.0.1", help="Http расширение и Ip")
    parser.addoption("--port", action="store", default="3006", help="Порт для API")
    parser.addoption("--path", action="store", default="/message/", help="Путь для API")
    parser.addoption("--maximize", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--remote", action="store_true")
    parser.addoption("--executor", action="store", default="http://127.0.0.1:4444")


log_map = {
    "DEBUG": logging.DEBUG
}


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    maximize = request.config.getoption("--maximize")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    remote = request.config.getoption("--remote")
    executor = request.config.getoption("--executor")

    class WebdriverListener(AbstractEventListener):
        logger = logging.getLogger(request.node.name)
        logger.setLevel(logging.INFO)
        ch = logging.FileHandler(filename=f"./logs/{request.node.name}.log")
        ch.setFormatter(logging.Formatter('%(name)s:%(levelname)s %(message)s'))
        ch.setLevel(log_map[log_level])
        logger.addHandler(ch)

        def before_navigate_to(self, url, driver):
            self.logger.info(f"I'm navigating to {url} and {driver.title}")

        def after_navigate_to(self, url, driver):
            self.logger.info(f"I'm on {url}")

        def before_navigate_back(self, driver):
            self.logger.info(f"I'm navigating back")

        def after_navigate_back(self, driver):
            self.logger.info(f"I'm back!")

        def before_find(self, by, value, driver):
            self.logger.info(f"I'm looking for '{value}' with '{by}'")

        def after_find(self, by, value, driver):
            self.logger.info(f"I've found '{value}' with '{by}'")

        def before_click(self, element, driver):
            self.logger.info(f"I'm clicking {element}")

        def after_click(self, element, driver):
            self.logger.info(f"I've clicked {element}")

        def before_execute_script(self, script, driver):
            self.logger.info(f"I'm executing '{script}'")

        def after_execute_script(self, script, driver):
            self.logger.info(f"I've executed '{script}'")

        def before_quit(self, driver):
            self.logger.info(f"I'm getting ready to terminate {driver}")

        def after_quit(self, driver):
            self.logger.info(f"Driver Quit")

    if browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        if remote:
            driver = webdriver.Remote(
                command_executor=executor,
                options=options
            )
        else:
            driver = webdriver.Firefox(options=options)
        driver.get(url)
        allure.attach(
            name=driver.session_id,
            body=json.dumps(driver.capabilities),
            attachment_type=allure.attachment_type.JSON)
    elif browser_name == "chrome":
        service = Service()
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        if remote:
            driver = webdriver.Remote(
                command_executor=executor,
                options=options
            )
        else:
            driver = webdriver.Chrome(service=service)
        driver.get(url)
        allure.attach(
            name=driver.session_id,
            body=json.dumps(driver.capabilities),
            attachment_type=allure.attachment_type.JSON)
    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("headless=new")
        if remote:
            driver = webdriver.Remote(
                command_executor=executor,
                options=options
            )
        else:
            driver = webdriver.Edge(options=options)
        driver.get(url)
        allure.attach(
            name=driver.session_id,
            body=json.dumps(driver.capabilities),
            attachment_type=allure.attachment_type.JSON)
    else:
        raise ValueError(f"Driver {browser_name} not supported.")
    driver = EventFiringWebDriver(driver, WebdriverListener())
    driver.test_name = request.node.name
    driver.log_level = log_level

    if maximize:
        driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="collapseBanner"]/div/div[3]/div[2]/button').click()
    yield driver
    driver.quit()


@pytest.fixture
def api_client(request):
    url = request.config.getoption("--url")
    port = request.config.getoption("--port")
    path = request.config.getoption("--path")

    base_url = f"{url}:{port}{path}"

    client = requests.Session()
    client.base_url = base_url

    yield client

    client.close()