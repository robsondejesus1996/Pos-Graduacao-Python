frutas1 = ['apple', 'banana', 'cherry', 'abacaxi']

'''frutas2 = []'''

'''for item in frutas1:
    if 'a' in item:
        frutas2.append(item)'''


frutas2 = [iten for iten in frutas1 if 'l' in iten]


print(frutas2)


print('---------------list comprehesion com numeros---------------')


'''valores = []'''

'''for x in range(6):
    valores.append(x * 10)


print(valores)'''


valores = [x * 10 for x in range(6)]
print(valores)


