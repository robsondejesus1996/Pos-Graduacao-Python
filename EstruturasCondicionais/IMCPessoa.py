print('--------------------------------')
print('Calculo do IMC - Indice de Massa Corporal')

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/ altura **2

if imc < 20:
    print("Seu peso esta abaixo do ideal. Seu IMC = {}".format(imc))
else:
    if imc >= 20 and imc<=25:
        print("Seu peso esta dentro da faixa ideal. Seu IMC = {}".format(imc))
    else:
        print("Seu peso esta cima do ideal. Seu IMC = {}.".format(imc))