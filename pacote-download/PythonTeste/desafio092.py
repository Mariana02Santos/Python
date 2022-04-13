from datetime import date
d = {}
d['Nome'] = str(input('Nome: '))
d['nasc'] = int(input('Ano de nascimento: '))
d['Idade'] = date.today().year - d['nasc']
d['CTPS'] = int(input('Carteira de trabalho [Digite 0 caso não possua]: '))
if d['CTPS'] != 0:
    d['Ano de contratação'] = int(input('Ano de contratação: '))
    d['Salário'] = float(input('Salário: '))
    d['Aposentadoria'] = 35 + d['Ano de contratação'] - d['nasc']
del d['nasc']
for k,v in d.items():
    print(f'{k}: {v}')

