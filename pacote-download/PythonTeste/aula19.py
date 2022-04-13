d = {'name':'mari','age':19,'gender':'feminine'}
del d['age']
print(d.values())
#    .keys()
#    .items()
for k,v in d.items():
    print(f'[{k}]:[{v}]')
print(d)

e = {}
br = []
for c in range(0,2):
    e['uf'] = str(input('estado: '))
    e['cidade'] = str(input('cidade: '))
    br.append(e.copy())
print(br)
