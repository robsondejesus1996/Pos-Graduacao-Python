'''
 Iniciar com letra, pode conter numeros, seprar _, letras minúsculas
'''

nome = 'Robson de Jesus'
idade = 27
altura = 1.8
e_maior = idade > 18
peso = 75

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))
print(e_maior, type(e_maior))
print(peso, type(peso))


print(idade * altura)


print('--------------Massa corporal--------------')
imc = peso / (altura**2)

print(nome, 'tem', idade, ' de idade e seu imc', imc)