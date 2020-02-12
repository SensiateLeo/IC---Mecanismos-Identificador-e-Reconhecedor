# -*- coding: utf-8 -*-
from selenium import webdriver


class Facebook:

    # metodo que prepara o teste
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.facebook.com/"

    # metodo que seleciona o form pelo id
    def get_form_by_id(self, driver, id_form):
        form = driver.find_element_by_id(id_form)
        # all_children_by_css = form.find_elements_by_id("email")
        # all_children_by_xpath = form.find_elements_by_xpath(".//*")
        # print(len(all_children_by_xpath))
        # for webElement in all_children_by_xpath:
        # print(webElement.tag_name, webElement.get_attribute("id"), webElement.get_attribute("class"))
        return form

    # metodo responsavel por realizar o teste
    def test_facebook(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        form = self.get_form_by_id(driver, "login_form")
        all_children_by_xpath = form.find_elements_by_xpath(".//*")

        # codigo que procura os nós do tipo input que possuem a substring "login" como valor de algum de seus atributos
        for childWebElement in all_children_by_xpath:
            if(childWebElement.tag_name == "input"): # procuramos todos nós do tipo input (descendentes do form)
                childWebElement_attributes_dict = driver.execute_script( # pegamos todos atributos e valores do input e criamos um dicionario
                    'var attr = {}; '
                    'for (index = 0; index < arguments[0].attributes.length; ++index) { '
                        'attr[arguments[0].attributes[index].name] = arguments[0].attributes[index].value ' 
                    '}; return attr;', childWebElement)
                for key, value in childWebElement_attributes_dict.items(): # iteramos por todas posições do dicionario (chave::valor ou key::value)
                    string_value = str(value)
                    if 'login' in string_value: # consultamos se o valor da dupla chave:valor da atual posição contem a substring 'login'
                     print(childWebElement_attributes_dict) # mostramos na tela os atributos dos inputs que contem a subtring
                     print(childWebElement)
                     print()

        self.driver.quit()


fbTest = Facebook()
fbTest.setUp()
fbTest.test_facebook()
