dado = input("Digite algo: ")
print("O tipo primitivo desse valor e ", type(dado))
print("So tem espacos ?", dado.isspace())
print("E um numero ? ", dado.isnumeric())
print("E alfabetico ?", dado.isalpha())
print("E alfanumerico ?", dado.isalnum())
print("Esta em maisculas ? ", dado.isupper())
print("Esta em minusculas ? ", dado.islower())
print("Esta capitalizada ? ", dado.istitle())