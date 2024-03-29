import random

numeros = [4, 5, 10, 34, 58, 59, 12, 15, 23, 32, 33, 46, 17, 20, 22, 35, 41, 42, 3, 35, 38, 40, 57, 58, 5, 10, 12, 18, 25, 33, 3, 6, 10, 17, 34, 37,
           5, 11, 22, 24, 51, 53, 2, 18, 31, 42, 51, 56, 1, 5, 11, 16, 20, 56, 20, 30, 36, 38, 47, 53, 14, 32, 33, 36, 41, 52, 3, 4, 29, 36, 45, 55,
           2, 10, 34, 37, 43, 50, 10, 27, 40, 46, 49, 58, 1, 11, 26, 51, 59, 60]


repetidos = []
ocorrencias = {}

for numero in numeros:
    if numero in ocorrencias:
        ocorrencias[numero] += 1
    else:
        ocorrencias[numero] = 1

for numero, quantidade in ocorrencias.items():
    if quantidade > 1:
        repetidos.append(numero)

#print("Números repetidos na lista:", repetidos)


listaRepetidos = [4, 5, 10, 34, 58, 59, 12, 32, 33, 46, 17, 20, 22, 35, 41, 42, 3, 38, 40, 18, 37, 11, 51, 53, 2, 56, 1, 36]


for nu in range(6):
    numeros_sorteio = random.sample(listaRepetidos, 6)
    print("Números sorteados:", numeros_sorteio)


'''
 Jogo 1: [8, 37, 39, 42, 45, 54]
 Jogo 2: [3, 9, 22, 24, 52, 56]
 Jogo 3: [7, 30, 38, 45, 48, 53]
 Jogo 4: [3, 16, 27, 28, 45, 53]
 Jogo 5: [6, 7, 26, 41, 58, 60]

Números sorteados: [3, 59, 4, 17, 41, 40]
Números sorteados: [3, 22, 58, 11, 42, 5]
Números sorteados: [56, 2, 4, 11, 58, 32]
Números sorteados: [1, 36, 53, 46, 20, 3]
Números sorteados: [20, 2, 11, 34, 53, 41]
Números sorteados: [56, 58, 1, 51, 53, 35]

'''



