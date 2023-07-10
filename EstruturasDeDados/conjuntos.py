print("----------------------------------------")
print("Como criar conjuntos")
conj_vazio1 = set() #Essa seria a unica forma de criar um conjunto vazio
conj_vazio2 = {} # as chaves sao utilizadas para construit um dicionario vazio
print(type(conj_vazio1))
print(type(conj_vazio2))

#criando os conjuntos
conj1 = {1, 2, 3, 4, 5, 6}
conj2 = {"A", "B", "C", "D"}
conj3 = {"ABC", 123, 2.14}

print(conj1)
print(conj2)
print(conj3)


print("----------------------------------------")
print("Como acessar elementos de um conjunto")

#conjuntos nao suportam indexacao. Entao vamos precisar do comando for para acessar os elementos de um conjunto
for elem in conj1:
    print(elem)


print("----------------------------------------")
print("Principais metodos de um obj conjunto")

#adicinando elementos ao conjunto
conj1.add(7)
print(conj1)

#visualizando os elementos de conj3
conj3.clear()
print(conj3)


#Copiando elementos de outro conjunto
conj3 = conj1.copy()
print(conj3)

#diferencas entre conjuntos
s1 = {1,2,3,4,5}
s2 = {4,5,6,7}

#atribui a s3 a diferenca do conjunto s1 em relacao a s2
s3 = s1.difference(s2)
print(s3)


#intersecao entre elementos
s4 = s1.intersection(s2)
print(s4)

#Verificando elementos disjuntos
print(s1.isdisjoint(s2))
print(s3.isdisjoint(s4))

#Verificando os subconjuntos
print(s1.issubset(s2))
print(s3.issubset(s1))


#verificando os superconjunto de s2
print(s1.issuperset(s2))
print(s1.issuperset(s3))

#remocao do 2 de conj usando o remove()
print(conj1)
conj1.remove(3)
print(conj1)

#removendo o 6 de conj1 usando o discard
conj1.discard(6)
print(conj1)

# Na secao foi realizada a intersecao de s1 e s2. Agora vamos calcular a diferenca simetrica
s5 = s1.symmetric_difference(s2)
print(s5)

#calculando o conjunto uniao. Elementos repetido so aparecem uma vez
s6 = s1.union(s2)
print(s6)

print("---------------------------------------------")
print("Funcoes aplicaveis a um conjunto")
print(s1)
print(len(s1))
print(max(s1))
print(min(s1))
print(sum(s1))


print("----------------------------------------------")
print("Conversao de uma lista em um conjunto")
lista = [1,2,3,4,5,6]

#convertendo a lista em um conjunto
conj_lista = set(lista)

#ao visualizar o conjunto objetdo atraves da conversao da lista, vemos que nao existem mais elementos repetidos
print(conj_lista)