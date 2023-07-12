print('--------------------------------')
print('O programa abaixo solicita que o usuario digite 3 lados de um suposto\n'
      'trinagulo. Depois de receber os valores dos 3 lados, ele verifica\n'
      'se os 3 lados formam ou nao formam um tringulo')

lado1 = float(input("Digite o 1o lado do triangulo:"))
lado2 = float(input("Digite o 2o lado do triangulo:"))
lado3 = float(input("Digite o 3o lado do triangulo:"))

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado3) and (lado3 + lado1 > lado2):
    if (lado1 == lado2) and (lado2 == lado3):  # tambem poderia usar iuf a==b==c
        print("Os lodos {}, {} e {} foram um tringulo equilatero.".format(lado1, lado2, lado3))
    elif (lado1 == lado2) or (lado2 == lado3) or (lado3 == lado1):
        print("Os lados {}, {} e {} foram um isoceles.".format(lado1, lado2, lado3))
    else:
        print("Os lados {}, {} e {} foram um tringulo escaleno.".format(lado1, lado2, lado3))
else:
    print("Os lados {}, {} e {} NAO foram um tringulo".format(lado1, lado2, lado3))
