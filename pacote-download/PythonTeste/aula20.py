def lin():
    print('-'*20)
lin()

def msg(m):
    lin()
    print(m)
    lin()
msg('SISTEMA')

def s(a,b):
    print(a+b)
s(2,3)

def cont(*num):
    for v in num:
        print(v,end=' ')
    print('\nfim')
cont(2,3,7)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6,4,5,8,2,7]
dobra(valores)
print(valores)

def soma(*val):
    s = 0
    for num in val:
        s += num
    print(s)
soma(3,6,4)
