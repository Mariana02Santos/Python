from random import randint
l = []
def maior(lst):
    lst.sort()
    print('Maior valor:',lst[len(lst)-1])

x = randint(1,10)

for c in range(0,x):
    l.append(randint(0,9))

maior(l)

