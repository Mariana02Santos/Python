d = {'nome':'0','media':0,'sit':'0'}
d['nome'] = str(input('Nome: '))
d['media'] = float(input('Média: '))
if d['media'] >= 7:
    d['sit'] = 'aprovado'
else:
    d['sit'] = 'reprovado'
print(d)


