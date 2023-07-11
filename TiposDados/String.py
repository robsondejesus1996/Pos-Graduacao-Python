#Criacao de uma string
nome = "Robson"
print(nome)
print(type(nome))
print(len(nome))

print("-------------------------------")
s = "Python"
print(s[0],s[1],s[2],s[3],s[4],s[5])

print("-------------------------------")
print("Slicing(fatiamento) em strings")
s = "Jupyter Notebook"

#retornando apenas a palavra jupyter - 1a opcao
print(s[0:7])



#Retornando apenas a palavra Jupyter - 2a opcao
print(s[-16:-9])


#retornando a palavra inteira
print(s[0:16])