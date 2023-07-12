print('--------------------------------')
print('Calculo do IMC - Indice de Massa Corporal')

peso = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / altura ** 2

if imc < 17:
    print("Seu peso esta muito baixo do ideal. Seu IMC = {}".format(imc))
elif imc >= 17 and imc < 18.5:
    print("Seu peso esta abaixo do ideal. Seu IMC = {}".format(imc))
elif imc >= 18.5 and imc < 25:
    print("Seu peso esta dentro da faixa ideal. Seu IMC = {}. ".format(imc))
elif imc >= 25 and imc < 30:
    print("Seu peso esta acima do ideal. Seu IMC = {}.".format(imc))
elif imc >= 30 and imc < 35:
    print("Seu peso esta acima do ideal (Obesidade I). Seu IMC = {}.".format(imc))
elif imc >= 35 and imc < 40:
    print("Seu peso esta acima do ideal (Obsidade II). Seu IMC = {}.".format(imc))
else:
    print("Voce vai morrer(Obsidade III - morbida), Seu IMC = {}.".format(imc))
