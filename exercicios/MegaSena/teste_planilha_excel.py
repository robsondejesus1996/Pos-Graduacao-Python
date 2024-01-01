from random import randint
from openpyxl import Workbook

lista = list()
jogos = list()

workbook = Workbook()
sheet = workbook.active

sheet['A1'] = '-'*60
sheet['A2'] = '-'*25 + ' MEGA SENA ' + '-'*24
sheet['A3'] = '-'*60

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

sheet['A4'] = '-=' * 3 + f' SORTEANDO {quant} JOGOS ' + '-=' * 3
for i, l in enumerate(jogos):
    l.sort()  # Ordenando os números de cada jogo
    cell = sheet.cell(row=i+5, column=1)
    cell.value = f' Jogo {i+1}: {l}'

sheet['A' + str(len(jogos) + 5)] = '-=' * 5 + ' < BOA SORTE! > ' + '-=' * 5

workbook.save(filename='resultados_mega_sena.xlsx')
