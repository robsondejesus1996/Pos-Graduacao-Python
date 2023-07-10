#criando dicionarios vazios
dic_vazio1 = {}
dic_vazio2= dict()

print(type(dic_vazio1))

print(isinstance(dic_vazio2, dict))

print('-----------------------------------------------------------')
#criacao de um dicionario
dic_estados = {"MG": "Minas Gerais", "PR": "Parana", "BA": "Bahia", "RN": "Rio Grande do Norte", "AM": "Amzonas"}
print(dic_estados)

dic_produtos = {1215:"Lapis", 3221: "Caneta", 2329:"Borracha"}
print(dic_produtos)

dic_notas_alunos = {"Joao": [30, 12, 21], "Maria": [20, 30, 29]}
print(dic_notas_alunos)

print('-----------------------------------------------------------')
print('Acessando um valor em um dicionario atraves de uma chave')
print(dic_estados["PR"])
print("Eu nasci em "+dic_estados["MG"])

#acessado o valor associado a chave 2329
print(dic_produtos[2329])

#acessando as notas associado a chave maria no dicionario dic_notas_alunos
nome_aluno = "Maria"
print(nome_aluno+ " tirou" +str(dic_notas_alunos[nome_aluno]))
print(nome_aluno+ " tirou " +str(dic_notas_alunos[nome_aluno][0])+ " pontos na 1a prova")

print('-----------------------------------------------------------')
print('Modificando valores em um dicionario')
print(dic_estados)

#corrigindo o nome do estado amazonas
dic_estados["AM"] = "Amazonas"
print(dic_estados)

print(dic_notas_alunos)
#alterando a segunda nota de Joao
dic_notas_alunos["Joao"][1] = 22
print(dic_notas_alunos)

print('-----------------------------------------------------------')
print('Principais metodos de um dicionario')
#crinado um dicionario ex
dic_exemplo = {1: "um", 2:"dois", 3:"tres", 4:"quatro"}
print(dic_exemplo)

#Removendo os elementos de dic_exemplo com o metodo clear()
dic_exemplo.clear()
print(dic_exemplo)


dic_exemplo = {1: "um", 2:"dois", 3:"tres", 4:"quatro"}
print(dic_exemplo)


#criando uma copia de dic_excemplo usando o metodo copy()
dic_exemplo2 = dic_exemplo.copy()
print(dic_exemplo2)

#Criando um novo dicionario a partir da selecao das chaves que desejamos
dic_num_pares = dict.fromkeys([2,4,6,8,10])
print(dic_num_pares)

# se desejarmos atribuir um valor default, basta informar apos a lista com as chaves
dic_num_pares = dict.fromkeys([2, 4, 6, 8, 10], "par")
print(dic_num_pares)


#metodo get retorna o valor associado a uma chave
print(dic_exemplo.get(2))

#Visualizando os pares chave/valor do dicionario
print(dic_exemplo.items())

#Visualizando as chaves de um dicionario
print(dic_exemplo.keys())

#removendo o par chave/valor associado a chave 1
dic_exemplo.pop(1)
print(dic_exemplo)

valor = dic_exemplo.pop(4)
print(dic_exemplo)
print(valor)

#Removendo o ultimo par chave/valor adicionado ao dicionario
removido = dic_num_pares.popitem()
print(removido)
print(dic_num_pares)


#Verificando o valor associado a chave "MG" e "ES"
print(dic_estados.setdefault("MG"))
print(dic_estados.setdefault("ES"))


#definindo o dicionario dic_estados_centro_oeste com alguns dos estados da regiao centro oeste
dic_estados_centro_oeste = {"MS": "Mato Grosso do Sul", "TO": "Tocantins", "GO": "Goias"}
print(dic_estados_centro_oeste)

#adicionando os estados do centro oeste ao dicionario dic_estados
dic_estados.update(dic_estados_centro_oeste)
print(dic_estados)

#Visualizando os valores de um dicionario
dic_estados.values()
