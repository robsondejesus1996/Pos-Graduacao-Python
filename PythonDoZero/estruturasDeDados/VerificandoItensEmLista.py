cores = ['amarelo','verde','azul','vermelho']

cor_cliente = input('Digite a cor desejada: ')

if cor_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Não tem em estoque')