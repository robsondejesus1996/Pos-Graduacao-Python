lista_idades = []
lista_pessoas = []
cont = 0

while (cont < 5):
    nome = input("Digite um nome: ")
    idade = int(input("Digite uma idade: "))
    lista_idades.append(idade)
    lista_pessoas.append(nome)
    cont = cont + 1

print("\n\nNomes digitados\n===============")
print(lista_pessoas)
print("\nIdades\n====================")
print(lista_idades)