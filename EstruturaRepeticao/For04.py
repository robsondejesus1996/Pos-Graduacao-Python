lista = [1, 19, 2, 15, 21, 12, 2]

soma_impar = 0
for n in lista:
        if n % 2 == 1:
            soma_impar = soma_impar + n
print("A soma dos elementos impares da lista = ", soma_impar)
