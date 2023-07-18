lista = [1, 19, 2, 15, 21, 12, 2]

cont_impar = 0
cont_par = 0
for num in lista:
    if num % 2 == 0:
        cont_par = cont_par + 1
    else:
        cont_impar = cont_impar + 1
print("A lista contem {} numeros pares e {} numeros impares.".format(cont_par, cont_impar))
