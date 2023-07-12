#criando uma lista vazia
lista_vazia = [0]
lista_vazia2 = list()

#visualizando o tipo
print(type(lista_vazia))
print(type(lista_vazia2))

#verificando o tamanho da lista
print(len(lista_vazia))

#crinado lista com elementos
lista = [11,2,3,4,5,6,7]
lista_reais = [1.5, -2.4]
lista_string = ['Robson', 'Maria', 'Marcondes']
lista_booleanos = [True, True, False, True]
lista_misturada = [1, 2, 3.9999, 'teste']
lista_misturada2 = [1,2, 3.1, 'teste', [1, "A", 1.0]]
lista_aninhadas = [ [1, 2, 3], [4, 5, 6]]

print(lista)
print(lista_reais)
print(lista_booleanos)
print(lista_misturada)
print(lista_misturada2)
print(lista_aninhadas)

#como acessar elementos de uma lista
print(lista[0])
print(lista_string[2])
print(lista_misturada[3])

#como modificar elementos de uma lista
lista[1] = 18
print(lista)

#principais metodos de um lista
lista.append(18) #para adicionar um elemento
print(lista)

lista_reais.clear()#para limpar os dados de uma lista
print(lista_reais)

#utilização do metodo copy para copiar os elementos de uma lista
copia = lista.copy()
print(copia)
copia[0] = 5

#utilização do metodo count para verificar quantidades espeficicas
print(copia.count(5))

#a maneira correta de adicionar novos elementos de uma lista, a partir de outra lista, é atraves de metodo extend()
numero = [1, 2, 3]
numero.extend([4,5])
print(numero)

#metodo insert() permite adicionar um elemento em qualquer posição da lista, caso a posição não exista, ele insere o elemento desejado na ultima posição
lista.insert(2, "ABC")
print(lista)

#metodo pop quando desejamos apgar uma posição da lista, removendo o elemento no indice 2
valor = lista.pop(2)
print(lista)


#metodo remove para quando desejarmos apagar um elemento específico da lista
print(lista_string)
lista_string.remove("Marcondes")
print(lista_string)


#metodo reserse para inverter os elementos de uma lista
lista = [1, 2, 3, 4, 5, 6]
lista.reverse()
print(lista)

#ordenação da lista com sort
lista.sort()
print(lista)


#elementos max e min de uma lista
print(min(lista))
print(max(lista))
