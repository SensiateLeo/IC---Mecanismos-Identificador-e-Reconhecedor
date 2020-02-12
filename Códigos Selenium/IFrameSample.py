from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.keys import Keys
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
"""


class IframeSample:

    def __init__(self, driver):
        self.driver = driver
        self.RUN = (By.ID, "run")
        self.EXPANDIR = (By.CSS_SELECTOR, "small a[href*=\"google\"]")
        self.HOME = (By.ID, "home")

    def find(self, *locator, timeout=30):
        return WebDriverWait(driver, timeout).until(visibility_of_element_located(*locator))

    def run(self):
        self.find(self.RUN).click()

    def expandir(self):
        self.driver.switch_to.frame("result")
        self.find(self.EXPANDIR).click()
        self.driver.switch_to.default_content()

    def home(self):
        self.find(self.HOME).send_keys(Keys.ENTER)

    def validar(self, url):

        assert self.driver.current_url == url


driver = webdriver.Firefox()
driver.get("https://jsfiddle.net/4b58ah85/7/")
test = IframeSample(driver)
test.run()
test.expandir()
test.home()
test.validar("https://jsfiddle.net/")
driver.quit()
