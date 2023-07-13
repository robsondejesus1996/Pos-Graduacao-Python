# Crie um algoritmo que leia um numero e mostre o seu dobro, tripo e raiz quadrada

numero = int(input("Informe um numero: "))
dobro = numero * 2
triplo = numero * 3
raiz = (numero ** (1/2))

#resultado
print("O numero informado: {}\n tem o seu dobro {}\n seu triplo {} \n raiz {:.2f}.".format(numero, dobro, triplo, raiz))
