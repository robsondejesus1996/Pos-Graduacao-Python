#Exercicio - Faca um programa que leia um numero inteiro e mostre na tela seu
#sucessor e seu antecessor

numero = int(input("Informe um numero: "))
sucessor = numero + 1
antecessor = numero - 1
print("Analisando o valor {}, seu antecessor e {} e o sucessor e {}".format(numero, antecessor, sucessor))