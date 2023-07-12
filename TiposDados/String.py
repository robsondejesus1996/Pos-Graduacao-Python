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

print("------------------------------------------")
print("Operadores aplicados a strings ")
s = "A linguagem Python e demais"
s1 = "Python"
print(s[0])# "A"
print(s[2:11]) # "Linguagem"
print(s[::-1])
s2 = s + " Sensacional!!!" #Concatenacao
print(s2)
s3 = s1*3 # Concatenando o string s1 3 vezes
print(s3)
print("O subtring '{}' esta contido em '{}' => {}".format(s1, s, s1 in s))
print("O subtring '{}' esta contido em '{}' => {}".format(s3, s2, s3 not in s2))


print("------------------------------------------")
print("String sao imutaveis")
print("vamos supor que queremos trocar um unico caractere digitado errado em um string")
s = "PythonM" #Python digitado com erro
#s[5] = "n" #tentando corrigir
#print(s)


print("------------------------------------------")
print("Metodos do objeto String")

s = "a linguagem python e demais"
print(s.capitalize())

#exemplo dos metodos casefold(), lower() e upper()
s = "AbCdEf"
s1 = s.casefold()
print(s1)

s2 = s.lower()
print(s2)

s3 = s.upper()
print(s3)

# casefold() e mais agressivo em sua conversao se comparado ao lower()
s4 = "Der Flub"
s5 = s4.casefold()
print(s5)

s6 = s4.lower()
print(s6)


#Exemplo do metodo center()
s = "PYTHON"
print(s)

s1 = s.center(20) # centralizar s em um string de tamanho 20 - completa com espacos a esquerda e direita
print(s1)

s2 = s.center(30, "*")# centralizar s em um string de tamanho 30 - completa com espacos a esquerda e direita
print(s2)

#Exemplo do metodo count()
s = "A linguagem Python e demais"
print(s.count("a"))
print(s.count("A"))

#Exemplo dos metodos endswith() e startswith()
s = "A linguagem Python e demais!"
print(s.endswith("demais"))

print(s.endswith("demais!"))


print("Exemplo dos metodos find(), rfind(), index() e rindex()")
s = "A linguagem Python e demais! Python e sensacional."
print(s.find("Python")) # Procura pelo subtring "Python" no string s usando o metodo find()
print(s.rfind("Python"))
print(s.index("Python"))
print(s.rindex("Python"))
print(s.find("Python"))
print(s.rfind("Python"))

s1 = "Ola Este e um exemplo. Este e outro exmplo"
print(s1.find("Este"))
print(s1.rfind("Este"))
print(s1.index("Este"))
print(s1.rindex("Este"))
print(s1.find("Este",15))



print("Exemplo do metodo format()")
nome = "Joaquim"
idade = 60
print("Meu nome e {} e tenho {} anos.".format(nome, idade))
print("Meu nome e {0} e tenho {1} anos.".format(nome, idade))
print("---------------------------------------------------------")
print("Meu nome e {} e tenho {} anos.\nRepetindo.. Meu nome e {} e tenho {} anos.".format(nome, idade, nome, idade))
print("Meu nome e {name} e tenho {age} anos.".format(age=18, name="Pedro"))


print("Exemplo do metodo isalnum()")
s = "D3C1FR4NDO"
print(s.isalnum())


print("Exemplo dos metodos islower() e isupper()")
s = "nome_aluno"
print(s.islower())
print(s.isupper())

s1 = "nomeAluno"
print(s1.islower())
print(s1.isupper())

s2 = "minha senh@ e 1234"
print(s2.islower)