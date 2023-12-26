valor = int (input('Digite um valor do produto: '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto sera de R${valor}')
    break
