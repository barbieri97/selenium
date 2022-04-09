from selenium import webdriver
import time
from selenium.common.exceptions import *

class agilefingers:
    def __init__(self, link):
        self.link = link
        self.driver = webdriver.Firefox(executable_path='path/to/geckodriver') # instacia o web driver
    
    def edita_texto(self, text):
        """ recebe um text em string e remove as quebras de linha """
        self.text = text
        texto = self.text.splitlines() # cria uma lista separando os items a cada \n e já tira os \n da lista
        texto_pronto = ' '.join(i for i in texto if i != '') # acrescenta a uma unica string todos os elementos não vazios da lista
        return texto_pronto 
    
    def coleta_texto(self):
        """ acessa o link e coleta o texto a ser digitado """
        self.driver.get(self.link) # acessa o link através do navegador
        texto = self.driver.find_element_by_id('textForTypingContent') # acessa a tag onde está o conteúdo a ser digitado
        texto_bruto = texto.text
        return texto_bruto
    
    def preencher(self,texto_pronto):
        """ começa a preencher os caracteres do texto na página """
        try:
            self.driver.find_element_by_id('goToTypingExercise').click() # clica no botão que leva para a pagina onde ira ocorrer a 'digitação'
            for i in texto_pronto:
                self.driver.find_element_by_id('insertedText').send_keys(i) # enviar para a tag de input cada caractere que há no texto
                time.sleep(0.03) # tempo para não sobrecarregar o navegador
        except ElementNotInteractableException: # tratar o erro que ocorre quando o tempo para digitar acaba
            print('o tempo acabou!')
    def start(self):
        """ deve-se iniciar o programa chamando essa função que já deixa tudo na ordem correta """
        texto_bruto = self.coleta_texto() # acessa a função para coletar o texto
        texto = self.edita_texto(texto_bruto) # edita o texto e devolve o texto pronto 
        self.preencher(texto) # faz a 'digitação'

if __name__ =='__main__':
    a = agilefingers('https://agilefingers.com/texts/alcott-louisa-may-little-women-en')
    a.start()