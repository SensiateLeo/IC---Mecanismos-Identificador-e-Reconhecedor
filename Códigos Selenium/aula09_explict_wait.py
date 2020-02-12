from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located,\
    \
    invisibility_of_element_located, title_contains, title_is, element_to_be_selected
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
"""

class LoginIn:

    def __init__(self, driver):
        self.driver = driver
        self.NOME = (By.ID, "name123")
        self.PASS = (By.ID, "pass123")
        self.SUBMIT = (By.CSS_SELECTOR, "button[class='form_submit'][type='submit']")
        self.RESULT = (By.CSS_SELECTOR, "div.w3-border")

    def find(self, *locator, timeout=30):
        return WebDriverWait(driver, timeout).until(visibility_of_element_located(*locator))

    def find_not(self, *locator, timeout=30):
        return WebDriverWait(driver, timeout).until(invisibility_of_element_located(*locator))

    def title_is(self, *locator, timeout=30):
        return WebDriverWait(driver, timeout).until(title_is(*locator))

    def login(self, user, password):

        self.find(self.NOME).send_keys(user)

        self.find(self.PASS).send_keys(password)

        self.find(self.SUBMIT).click()

    def validar(self, value01, value02):

        self.find_not(self.SUBMIT)

        assert self.title_is(value01)

        elem = self.find(self.RESULT)

        assert value02 in elem.text


driver = webdriver.Firefox()
driver.get("http://localhost:8083/Documents/IC/Curso_Selenium/HTML/login.html")
test = LoginIn(driver)
test.login("Leonardo", "12345")
test.validar("Forms action page", "uname=Leonardo&psw=12345")
sleep(5)
driver.quit()
