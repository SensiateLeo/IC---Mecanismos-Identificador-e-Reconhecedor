from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
"""

driver = webdriver.Firefox()
driver.maximize_window

driver.get("http://127.0.0.1:8083/Documents/IC/Curso_Selenium/Selenium/alert_tests/html/prompt.html")

driver.implicitly_wait(10)

test = driver.find_element("id","prompt")
test.click()
sleep(5)
alert = Alert(driver)
print(alert.text)
sleep(3)
nome = "Leonardo Sensiate"
alert.send_keys(nome)
alert.accept()

test2 = driver.find_element("id","demo")
assert test2.text == nome

sleep(10)
driver.quit()