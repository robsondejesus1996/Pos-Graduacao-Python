from random import randint
from time import sleep

lista = list()
jogos = list()

with open('resultados_mega_sena.txt', 'w') as arquivo:
    arquivo.write('-' * 60 + '\n')
    arquivo.write('-' * 25 + ' MEGA SENA ' + '-' * 24 + '\n')
    arquivo.write('-' * 60 + '\n')

    quant = int(input('Quantos jogos foram realizados: '))
    tot = 1

    while tot <= quant:
        cont = 0
        while True:
            num = randint(1, 100)  # 1 até 60
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= 20:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1

    arquivo.write('-=' * 3 + f' SORTEANDO {quant} JOGOS ' + '-=' * 3 + '\n')
    for i, l in enumerate(jogos):
        jogo = f' Jogo {i + 1}: {l}\n'
        arquivo.write(jogo)
        # sleep(1)
    arquivo.write('-=' * 5 + ' < BOA SORTE! > ' + '-=' * 5 + '\n')
