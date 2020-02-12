from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()

driver.switch_to.alert.authenticate('cheese', 'secretGouda')

# verifica se realizou o teste com sucesso.
html = driver.page_source
assert "reinaldorossetti.blogspot.com" in html

# pedir pro browser sair.
driver.quit()

