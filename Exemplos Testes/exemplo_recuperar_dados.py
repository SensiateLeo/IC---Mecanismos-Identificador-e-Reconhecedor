from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import json

class Teste:

    def __init__(self, driver):
        self.driver = driver

    # Disparada dos eventos
    def dispara_eventos(self):
        driver = self.driver

        # Abrir a janela modal
        abrir = driver.find_element_by_id("opener")  # Botão que abre a janela Modal
        fechar = driver.find_element_by_css_selector(".ui-button-icon")  # Botão que fecha a janela
        ActionChains(driver).click(abrir).click(fechar).perform()  # Abre e fecha a janela
        driver.switch_to.default_content()  # Retorna o foco para a página principal
        sleep(4)

        # Clicar no calendario
        calendario = driver.find_element_by_id("datepicker")  # Elemento que abre o calendário
        calendario.send_keys("teste")
        sleep(2)
        calendario.click()
        mes = driver.find_element_by_css_selector(".ui-icon-circle-triangle-e")  # Botão que troca o mês do calendário
        mes.click()
        data = driver.find_element_by_xpath("//a[contains(.,'4')]")  # Botão que seleciona a data (dia/mes/ano)
        data.click()

#Instancia o browser
driver = webdriver.Firefox()
driver.implicitly_wait(30)

#Script que configura/ inicia o MutationObserver
poe = open("mutation_observer.js", "r")
set_mut = poe.read()

#Script que configura/ inicia o MutationObserver
#poe = open("M_O2.js", "r")
#set_mut = poe.read()

#fecha = open("fecha_mo.js", "r")
#fecha_mut = fecha.read()

#Script que captura os elementos que sofreram mutações
pega = open("get_mutation.js", "r")
get_mut = pega.read()

#Script que captura o tipo das mutações identificadas
tipo = open("get_tipos.js", "r")
tipo_mut = tipo.read()

#Acessa a página criada para teste
driver.get("http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html")

teste = Teste(driver)
driver.execute_script(set_mut) #Ativa o mutationObserver
teste.dispara_eventos() #Realiza o disparo dos eventos
#driver.execute_script(fecha_mut)
sleep(3)
tipos_capt = driver.execute_script(tipo_mut) #Recupera o tipo das mutações identificadas
targets = driver.execute_script(get_mut)  #Recupera as mutações identificadas

i = 0

#Realiza o print das mutações juntamente com o tipo de mutação detectada
#while(i < tipos_capt.__len__()):
#    print("Tipo: ", tipos_capt[i])
#    print("Mutação: ", targets[1], "\n")
#    i = i + 1

for i in range(len(tipos_capt)):
    print(tipos_capt[i].screenshot("saida.png"))
#driver.quit() #Encerra o browser - está comentado para que o console do browser fique acessível
