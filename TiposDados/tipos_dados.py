print('Tipos de dados em Python')

print('tipo inteiro')
idade = 18
ano = 2002
print(type(idade))
print(type(ano))
print('------------------------------------')

print('Ponto flutuante ou Decimal(float)')
altura = 1.80
peso = 73.55
print(type(peso))
print(type(altura))
print('------------------------------------')


print('Complexo(complex)')
a = 5+2j
b = 20+6j
print(type(a))
print(type(b))
print(complex(2, 5))
print('------------------------------------')

print('String(str)')
name = 'Robson'
profissao = 'Engenhiro de Software'

print(type(profissao))
print(type(name))
print('------------------------------------')


print('Boolean(bool)')
fim_de_semana = True
feriado = False
print(type(fim_de_semana))
print('------------------------------------')


print('Listas')
alunos = ['Amanda', 'Ana', 'Bruno', 'João']
notas = [10, 8.5, 7.8, 8.0]
print(type(alunos))
print(type(notas))
print('------------------------------------')


print('Tuplas(tuple)')
valores = (90, 79, 54, 32, 21)
pontos = (100, 94.05, 86.8, 62)
print(type(valores))
print(type(pontos))
print('Caso haja tentativa de alterar os itens de uma tupla após sua definição com no código a seguir')
#tuple = (0, 1, 2, 3)
#tuple = [0] = 4
print('------------------------------------')

print('Dicionários(dict)')
altura = {'Amanda': 1.65, 'Ana': 1.60, 'João': 1.70}
peso = {'Amanda': 60, 'Ana': 58, 'JOão': 68}
print(type(altura))
print(type(peso))
print('------------------------------------')


print('Como mudar o tipo de uma variavel')
print('Decimal(float) para String(str)')
altura = 1.80
print(type(altura))

#conversão do tipo
altura = str(altura)
#depois da conversão
print(type(altura))
print(altura)

print('------------------------------------')
print('Inteiro (int) para Decimal (float)')
#antes da conversão
idade = 18
print(idade)
print(type(idade))

#conversão do tipo
idade = float(idade)

#depois da conversão
print(type(idade))
print(idade)
print('------------------------------------')


print('------------------------------------')
print('Booleano(bool) para Inteiro(int)')
#antes da conversão
fim_de_semana = False
print(type(fim_de_semana))

#conversão do tipo
fim_de_semana = int(fim_de_semana)

#depois da conversão
print(type(fim_de_semana))
print(fim_de_semana)
print('------------------------------------')


print('teste conversão de booleano')
teste_booleano = "False"

#conversão do tipo
teste_booleano = bool("")
print(type(teste_booleano))
print(teste_booleano)
#logo sempre será verdadeiro quando tiver algo dentro dessa variavel, se não tiver nada vai ser considerado falso .
print('------------------------------------')

