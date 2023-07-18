soma = 0
qtde = 0
den = 0
termo = 1

while (termo > 0.0001):
    qtde += 1
    den = qtde ** 2
    termo  = 1 / den
    soma += termo
    print("{} o termo {}/{} = {}".format(qtde, 1, den, termo))
print(soma)