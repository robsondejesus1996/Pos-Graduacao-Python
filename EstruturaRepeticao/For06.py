# maior palavra da lingua portuguesa
maiorpalavra = 'pneumoultramicroscopicossilicovulcanoconiótico'
for letra in maiorpalavra:
    print(letra)

# iterando sobre uma tupla
tupla = (1, 19, 5, 12, 6)
for ele in tupla:
    print(ele)

print("-------------------------------------------")
conj1 = {1, 5, 2, 6, 3, 4}
for ele in conj1:
    print(ele)
print("-------------------------------------------")

conj2 = {1, 17, 12, 4, 2, 20}
for ele in conj1:
    print(ele)
print("-------------------------------------------")

conj2 = {1, 17, 12, 4, 2, 20}

for ele in conj1:
    if ele in conj2:
        print("O elemento {} esta contido em conj1.".format(ele))
    else:
        print("O elemento {} nao esta contido em con2.". format(ele))

print("-------------------------------------------")

#iterando em um dicionario

dic_estados = { "MG": "Minas Gerais", "PR": "Parana", "BA": "Bahia", "RN": "Rio Grande do Norte", "AM": "Amazonas"}
for est in dic_estados:
    print(est)
print("-------------------------------------------")
for est in dic_estados.values():
    print(est)
print("-------------------------------------------")

for (sig,est) in dic_estados.items():
    print("A sigla para {} e {}.".format(est, sig))
print("-------------------------------------------")

print('Comprehensions')
print("Uma maneira bastante cocisa que o py fornece para a criacao de sequenciar(listas, tuplas, dicionarios)")

lista3 = []
for i in range(1, 21):
    lista3.append(i)
print(lista3)