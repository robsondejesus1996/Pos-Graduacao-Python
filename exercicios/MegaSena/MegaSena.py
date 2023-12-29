#61 ate 121
#1 até 60

#contator = 1
#for i in range(61, 121):
#    print(i, 'Esta na posição' ,contator)
#    contator+=1
#print("Contator " , contator )


from random import randint
from time import sleep

lista = list()
jogos = list()

print('-'*60)
print('-'*25,'MEGA SENA','-'*24)
print('-'*60)
quant = int(input('Quantos jogos foram realizados: '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60) #1 até 60
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' *3)
for i, l in enumerate(jogos):
    print(f' Jogo {i+1}: {l}')
    sleep(1)
print('-=' *5, '< BOA SORTE! >', '-=' *5)



