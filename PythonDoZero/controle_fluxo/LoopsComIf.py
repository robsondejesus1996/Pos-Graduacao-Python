compra_confirmada = False
dados_compra = 'Comprar no valor de R$12.50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes Enviado para o seu e-mail')
        break
else:
    print("Falha na Compra")