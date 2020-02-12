from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
"""

driver = webdriver.Firefox()
driver.maximize_window

driver.get("http://127.0.0.1:8083/Documents/IC/Curso_Selenium/Selenium/alert_tests/html/confirm.html")

driver.implicitly_wait(10)

test = driver.find_element("id", "alert")
test.click()
sleep(5)
alert = Alert(driver)
alert.dismiss()

driver.get("http://127.0.0.1:8083/html/confirm.html")
driver.implicitly_wait(10)

test = driver.find_element("id", "confirm")
test.click()
sleep(5)
alert = Alert(driver)
alert.dismiss()
test = driver.execute_script("return test")
print(test)

driver.quit()