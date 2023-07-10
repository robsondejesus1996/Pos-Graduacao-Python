tupla_vazia = ()
tupla_vazia2 = tuple()

#verificando o tipo de tupla
print(type(tupla_vazia))

#verificando se tupla_vazia2 e uma instancia de dupla
print(isinstance(tupla_vazia2, tuple))

#verificando a quantidade de elementos na tupla
print(len(tupla_vazia))

#criacao de tuplas com elementos
print('-----------------------------------------------------')
tupla1 = (3, 19, 4, 21, 3, 13)
tupla2 = (3, 19, 4, 21, 3, 5, 13, "tupla", (1, 2, 3))
tupla3 = (3, 19, 4, 21, 3, 5, 13, "tupla", [1, 2, 3])
print(tupla1)
print(tupla2)
print(tupla3)
print('-----------------------------------------------------')

#acessando o indice 0 (primeira posicao) de tupla1
print('Indice o da tupla:',tupla1[0])

#acessando elementos tupla 2
print('Acessando o indice 5 da tupla2:', tupla2[5])

#vai dar erro
#print(tupla1[20])

#acessando o indice 8 (nova posicao) de tupla3
print('Elemento tupla3: ',tupla3[8])

print('-----------------------------------------------------')
print('Teste de imutabilidade de uma tupla')
#tupla1[0] = 5
#print(tupla1)
#vai dar erro nao da pra mudar nada em uma tupla

tupla3[8].extend([4,5,6])
print(tupla3)
print('-----------------------------------------------------')
print('Principais metodos de um objeto tupla')
#quantidade de elementos que tem na tupla
print(tupla1.count(3))

#metodo index em que posicao esta armazenado o elemento 21
print(tupla1.index(21))

print('Funcoes aplicaveis a uma tupla')
print('Elementos da tupla 1: ', tupla1)
print(len(tupla1))
print(max(tupla1))
print(min(tupla1))
print(sum(tupla1))


print('-----------------------------------------------------')
print('Convertendo uma tupla em lista')
lista = list(tupla1)
print(lista)
lista[5] = - 1
print('Novos elementos da lista: ', lista)