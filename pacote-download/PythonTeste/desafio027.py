n = input('Nome completo: ')
x = n.split()
print('Primeiro nome:', x[0])
y = n.count(' ')
print('Último nome:', x[y])
#print('Último nome:', x[len(x) - 1])
