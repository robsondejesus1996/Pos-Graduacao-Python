print("Adicao", 3+2)
print("Subtracao", 7-5)
print("Multiplicacao", 2*3)
print("Divisao", 9/3)
print("Divisao - Calculando o coeficinete", 5//2)
print("Divisao - Calculando o resto", 5%2)
print("Potenciacao", 3 ** 2)
print("Radiciacao raiz quadrada de 9", 9 ** (1/2))
print("Raiz quadrada de 16 (elevando a 0.5 ao inves da fracao 1/2)", 16 ** 0.5)
print("Raiz cubica de 27", 27 ** (1/3))
print("--------------------------------------------------------------------------")
print("Exercicios de fixacao")
print("Operacao 1:", 2 + 3 * 4 / 5 - 6)
print("Operacao 2:", (2 + 3)* 4/(5-6))
print("Operacao 3:", ((2-3)**2/4)**(1/2))

print("--------------------------------------------------------------------------")
print("Criacao de variaveis")
idade = 47
nome = 'Jose Maria da Silva'
salario = 3.14159
aprovado = True
print("Nome:", nome , "idade:", idade, "salario", salario, "aprovado:", aprovado)
#utilizacao do metodo format
print('Meu nome e {} e tenho {} anos'.format(nome, idade))

print("--------------------------------------------------------------------------")
print("Calculado da area e perimeto do retangulo")
base = 7
altura = 8
area = base * altura
perimetro = 2 * (base + altura)
print(area)

print("--------------------------------------------------------------------------")
print("Calculo da area e comprimento da circunferencia")
raio = 2
area = 3.14159 * raio ** 2
comprimento = 2 * 3.1419 * raio
print('Para o raio {}, a area = {} e o comprimento = {}'. format(raio, area, comprimento))

print("--------------------------------------------------------------------------")
print("Calculo da distancia euclidiana entre 2 pontos no plano cartesiano")
print("Calculando a distancia entre os pontos (3,4) e (5,6)")
x1 = 3
y1 = 4
x2 = 5
y2 = 6
dist = ((x1 - x2)**2 + (y1-y2)**2)**(1/2)
print('A distancia entre os pontos({},{}) e ({},{}) = {}.'.format(x1, y1, x2, y2, dist))


print("--------------------------------------------------------------------------")
print("Calculo do delta e das raizes de uma equacao do segundo grau")
print("Calculando o Delta e raizes x1 e x2 para equacao y = x**2 - 5x +6")
a = 1
b = -5
c = 6
delta = b**2 - 4*a*c
x1 = (-b+delta**(1/2))/(2*a)
x2 = (-b-delta**(1/2))/(2*a)
print('Delta = {}, x1 = {} e x2 = {}'.format(delta, x1, x2))


print("--------------------------------------------------------------------------")
print("Calculo da area do setor circular (fatia de um circulo)")
print("Para um circulo de raio 15, calcular a area de uma fatia com angulo = 45 graus(uma pizza)")
print("Isso equivale a calcular a area de uma das 8 fatias de uma pizza com 30 cm de diamentor")
a = 45
r = 15
s = (a * 3.14159 * r ** 2)/360
print('Num circulo de raio {}cm, setor circular de angulo {} tera area = {} cm^2.'.format(r,a,s))
