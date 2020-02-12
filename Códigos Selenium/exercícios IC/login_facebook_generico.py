from selenium import webdriver
from time import sleep


class LoginSenha:

#Passamos para a classe o driver e o id do formulario buscado como parametros de sua criação
    def __init__(self, driver, form_buscado):
        self.driver = driver
        self.form_buscado = form_buscado

#Função responsavel por identificar os elementos, colocar e enviar os dados para o login
    def enviar_dados(self, user, password):
        driver = self.driver

        elementos = driver.find_elements_by_css_selector("*") #Cria um vetor com todos os elementos presentes na página ('*' serve para selecionar todos)
        for webElement in elementos: #Percorremos o vetor de elementos
            if webElement.get_attribute("id") == self.form_buscado: #Verificação: Verifica se algum dos elementos da página contém o id passado como parâmetro da classe LoginSenha
                form = driver.find_element_by_id(webElement.get_attribute("id")) #Se esse elemento é encontrado, retorna- o na variável form
                break

        children_xpath = form.find_elements_by_xpath(".//*") #Cria um vetor com todos os nós "filhos" do form atribuído anteriormente
        comandos = 0 #Variavel que controla a quantidade de comandos enviados à página html (Neste caso queremos 3 comandos)
        for webElement in children_xpath:  #Percorremos o vetor de children

            if ('email' in webElement.get_attribute("id") or 'login' in webElement.get_attribute("id")): #Verificação: Verifica se o id contem 'email' ou 'login' e se é do tipo input, então este elemento é o que queremos
                if webElement.tag_name == "input":
                    webElement.send_keys(user) #Envia o texto 'user' passado como parâmetro ao campo no qual ele deve ser escrito
                    comandos = comandos + 1

            if ('pass' in webElement.get_attribute("id") and webElement.tag_name == "input"):  #Verificação: se o id contem 'pass' e é do tipo input, então este elemento é o que queremos
                webElement.send_keys(password) #Envia o texto 'password' passado como parâmetro ao campo onde deve ser escrita a senha
                comandos = comandos + 1

            if webElement.get_attribute('type') == 'submit' and webElement.tag_name == "input":
                webElement.click() #Aplica um clique do mouse sobre o botão cujo tipo é 'submit'
                comandos = comandos + 1

            if comandos == 3: #Se os três comandos já foram enviados, sai do for
                break


driver = webdriver.Firefox()

driver.implicitly_wait(30)
driver.get("https://www.facebook.com/")
teste = LoginSenha(driver, "login_form") #'login_form' é o id do form que estamos buscando dentro da página
teste.enviar_dados("login", "senha") #'login' e 'senha' são os parâmetros que desejamos escrever nas caixas- texto da área de login do site
sleep(5)
driver.quit()
