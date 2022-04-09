# AUTOMAÇÃO COM SELENIUM

Procurando um site para treinar a velocidade da digitação e assim aumentar a produtividade achei um site muito bom o agilefingers.com.

Durantes os treinamentos vi uma oportunidade de aprimorar minhas habilidades de web scraping, criar com o Selenium um programa que faça a digitação automática dos textos.

O programa tem apenas cinco funções:

* `__init__`: é passado o link que irá ser acessado e já é seatado o web driver.
* `coleta_texto`: acessa o link que foi passado ao instaciar a classe e faz o scrapy do texto a ser "digitado".
* `edita_texto`: recebe o texto que foi coletado e formata ele para ser "digitado".
* `preencher`: recebe o texto editado pela função `edita_texto` e começa a digitar o texto .
* `start`: inicia o programa chamando as funções e passando os parametros de forma correta.

## ATENÇÃO

Esse programa tem como intuito somente desenvolver o conhcimeto sobre scraping e automação 
não é a intenção obter vantagem de qualquer tipo