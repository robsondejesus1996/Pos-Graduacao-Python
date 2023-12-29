lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 60, 70]

num1 = set(lista1)
num2 = set(lista2)

print(num1 | num2) # Uniao
print(num1 - num2) # Diferença
print(num1 ^ num2) # Diferença simetrica
print(num1 & num2) # And

print(len(num1))
