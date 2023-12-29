aluno = {'nome': 'Ana', 'idade': 15, 'nota_final': 'A', 'aprovação': True}

aluno['nome'] = 'Jose'
print(aluno)


aluno.update({'nome': 'Robson', 'nota_final': 'B'})
print(aluno)

aluno.update({'endereco': 'Rua a'})
print(aluno)

print(aluno.get('sexo', 'Não existe'))

del aluno['endereco']
print(aluno)