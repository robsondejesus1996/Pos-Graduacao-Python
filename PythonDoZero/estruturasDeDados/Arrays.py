from array import array

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40, 50, 60]
numeros_f = [1.2 , 2.2, 3.3]

print(letras)
print(numeros_i)
print(numeros_f)

print()

letras = array('u', ['a', 'b', 'c', 'd'])
print(letras)

nuemros_i = array('i', [10, 20, 30, 40, 50, 60])
print(nuemros_i)

numeros_f = array('f', [1.2 , 2.2, 3.3])
print(numeros_f)
