'''
* Criar variaveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variavel com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casa decimais (peso e na altura da pessoa
* Exibir um texto com todas os valores na tela usando F-String (com as chaves)
'''
import datetime

nome = 'Robson de Jesus'
idade = 28
altura = 1.8
peso = 75.0
ano_atual = datetime.datetime.now().year
idade_pessoa = ano_atual - idade
imc = peso / (altura**2)

print(f'{nome} tem {idade} anos de idade, com {altura} de altura e um peso de {peso} kg. \n O imc de {nome} é de {imc:.2f} \n {nome} nasceu em {idade_pessoa}')



