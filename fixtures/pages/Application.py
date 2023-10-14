import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import allure


class Application:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.7).click().perform()

    def _input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        try:
            return self.element(parent_locator).find_element(*child_locator)
        except NoSuchElementException:
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG
                          )
            raise AssertionError(f"Не найден элемент {child_locator} в {parent_locator}")

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG
                          )
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG
                          )
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    def verify_product_item(self, product_name):
        return self.element((By.LINK_TEXT, product_name))
