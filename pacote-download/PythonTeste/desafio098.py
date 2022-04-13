from math import fabs

def cont(a,b,c):
    cont = a

    if b > a:
        if c == 0:
            c = 1
        if c < 0:
            c = fabs(c)
        while cont <= b:
            print(int(cont),end=' ')
            cont += c
    else:
        if c == 0:
            c = -1
        while cont >= b:
            print(int(cont),end=' ')
            cont -= abs(c)

x = int(input('Início: '))
y = int(input('Fim: '))
z = fabs(int(input('Pula: ')))

cont(x,y,z)






