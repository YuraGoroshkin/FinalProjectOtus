from selenium.webdriver.common.by import By
from fixtures.pages.Application import Application
from faker import Faker
from time import sleep
import allure

fake = Faker()


class HomePage(Application):
    def submit_form(self, name=f"{fake.name()}", email=f"{fake.email()}", phone=f"{fake.phone_number()}", subject=f"{fake.name()}", description=""):
        self.find_element(By.XPATH, "//*[@data-testid='ContactName']").send_keys(name)
        self.find_element(By.XPATH, "//*[@data-testid='ContactEmail']").send_keys(email)
        self.find_element(By.XPATH, "//*[@data-testid='ContactPhone']").send_keys(phone)
        self.find_element(By.XPATH, "//*[@data-testid='ContactSubject']").send_keys(subject)
        self.find_element(By.XPATH, "//*[@data-testid='ContactDescription']").send_keys(description)
        self.find_element(By.XPATH, "//*[@id='submitContact']").click()

    def get_acces_submit_form(self):
        sleep(0.1)
        data = self.find_element(By.XPATH, "//*/div[@class='col-sm-5']/div/h2").text
        print(data)
        return data

    def get_alert_submit_form(self):
        sleep(0.1)
        data = self.find_element(By.XPATH, "//*[@class='alert alert-danger']").text
        print(data)
        return data
