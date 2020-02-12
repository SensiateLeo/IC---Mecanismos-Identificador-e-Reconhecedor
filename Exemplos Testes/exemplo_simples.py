from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

#Classe principal (contém o driver)
class Teste:

    def __init__(self, driver):
        self.driver = driver

    # Disparada dos eventos
    def dispara_eventos(self):
        driver = self.driver

        #Abrir a janela modal
        abrir = driver.find_element_by_id("opener") #Botão que abre a janela Modal
        fechar = driver.find_element_by_css_selector(".ui-button-icon") #Botão que fecha a janela
        ActionChains(driver).click(abrir).click(fechar).perform() #Abre e fecha a janela
        driver.switch_to.default_content() #Retorna o foco para a página principal
        sleep(4)

        #Clicar no calendario
        calendario = driver.find_element_by_id("datepicker") #Elemento que abre o calendário
        calendario.send_keys("teste")
        sleep(2)
        calendario.click()
        mes = driver.find_element_by_css_selector(".ui-icon-circle-triangle-e")#Botão que troca o mês do calendário
        mes.click()
        data = driver.find_element_by_xpath("//a[contains(.,'4')]")#Botão que seleciona a data (dia/mes/ano)
        data.click()

#Instancia o browser
driver = webdriver.Firefox()
driver.implicitly_wait(30)

#Script que configura/ inicia o MutationObserver
poe = open("mutation_observer.js", "r")
set_mut = poe.read()

#Script que captura os elementos que sofreram mutações
pega = open("get_mutation.js", "r")
get_mut = pega.read()

#Script que captura o tipo das mutações identificadas
tipo = open("get_tipos.js", "r")
tipo_mut = tipo.read()

#Acessa a página criada para teste
driver.get("http://cafe.intermidia.icmc.usp.br:22080/leonardo/site_exemplo.html")

driver.execute_script(set_mut) #Ativa o mutationObserver
teste = Teste(driver)
teste.dispara_eventos() #Realiza o disparo dos eventos
url = driver.current_url
print(url)
sleep(3)
tipos_capt = driver.execute_script(tipo_mut) #Recupera o tipo das mutações identificadas
targets = driver.execute_script(get_mut)  #Recupera as mutações identificadas

i = 0
j = 0

#Realiza o print das mutações juntamente com o tipo de mutação detectada
while(i < tipos_capt.__len__() and j < targets.__len__()):
    print("Mutacão", i)
    print("Tipo: ", tipos_capt[i])
    print("Elemento: ", targets[j], "\n")
    i = i + 1
    j = j + 1
#Para visualizar de uma maneira mais clara as mutações e os elementos responsáveis por elas,
#acessar o console do browser ao fim da execução do teste

#driver.quit() #Encerra o browser - está comentado para que o console do browser fique acessível
