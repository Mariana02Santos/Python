l = ['a','b','c']
p = list()
p.append(l[:])
print(p)

v = [['a',1],['a',2]]
print(v)
print(v[0][0])

teste = []
teste.append('a')
teste.append(0)
t = []
t.append(teste[:])
print(t)
teste[0] = 'b'
teste[1] = 1
t.append(teste)
print(t)

galera = []
dado = []
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)



