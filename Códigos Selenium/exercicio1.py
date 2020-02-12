from selenium import webdriver
from time import sleep

"""
Levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
"""


class LoginSenha:

    def __init__(self, driver, form_buscado):
        self.driver = driver
        self.form_buscado = form_buscado

    def enviar_dados(self, usuario, password):
        driver = self.driver
        form = driver.find_element_by_tag_name("form")
        form.find_element_by_id("name123").send_keys(usuario)
        form.find_element_by_id("pass123").send_keys(password)
        form.find_element_by_css_selector("button[class='form_submit'][type='submit']").click()


driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get("http://localhost:8083/Documents/IC/Curso_Selenium/HTML/login.html")
teste = LoginSenha(driver, "form")
teste.enviar_dados("login", "senha")
sleep(5)
driver.quit()
