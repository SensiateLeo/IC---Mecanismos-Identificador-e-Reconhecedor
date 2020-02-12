﻿from selenium import webdriver
from selenium.webdriver.common.by import By
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
"""

driver = webdriver.Firefox()

driver.get("http://localhost:8083/Documents/IC/Curso_Selenium/HTML/login.html")


driver.find_element(By.ID, "name123").send_keys("Reinaldo")

driver.find_element(By.ID, "pass123").send_keys("12345")

driver.find_element(By.CSS_SELECTOR, "button[class='form_submit'][type='submit']").click()

elem = driver.find_element(By.CSS_SELECTOR, "div.w3-border")

assert "uname=Reinaldo&psw=12345" in elem.text

driver.quit()

