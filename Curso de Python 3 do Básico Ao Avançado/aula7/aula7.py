nome = 'Robson de Jesus'
idade = 27
altura = 1.8
e_maior = idade > 18
peso = 75
imc = peso / (altura**2)


print(f'{nome} tem {idade} anos de idade e seu peso é de {peso} e uma massa coorporal de {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))