# Iterando sobre uma faixa de valores gerada com a funcao range()
for i in range(5):
    print(i)

print("------------------------------------------")

soma_mult_3 = 0
for x in range(3, 100, 3):
    soma_mult_3 += x
print(soma_mult_3)
print("------------------------------------------")
print("Imprimindo a taboada de um numero qualquer")

num = int(input("Digite o numero que deseja imprimir a taboada: "))
for mult in range(1, 11):
    print("{} x {} = {}".format(num, mult, num*mult))

print("------------------------------------------")
print("Imprimindo a taboada de 1 a 9")
for num in range(1, 10):
    for mult in range(1,11):
        print("{} x {} = {}".format(num, mult, num*mult))
print("------------------------------------------")