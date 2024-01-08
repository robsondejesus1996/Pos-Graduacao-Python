valores = [10, 12, 34, 44, 57]

#filtrar valores abaixo de 20

'''def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))'''

print(list(filter(lambda x: x > 20, valores)))