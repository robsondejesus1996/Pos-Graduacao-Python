#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2)/2
print("Primeira nota do aluno: {}".format(nota1))
print("Segunda nota do aluno: {}".format(nota2))
print("A media entre {:.1f} e {:.1f} seria igual a {:.1f}".format(nota1, nota2, media))