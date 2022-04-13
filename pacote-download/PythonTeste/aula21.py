#help()
#help(print)
#print(input.__doc__)
def cont(i,f,p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(c)
        c += p
help(cont)

def somar(a=0,b=0,c=0):
    s = a+b+c
    return s

resp = somar(3,2,5)
#print(somar(3,2,5))
r1 = somar(3,2,6)
r2 = somar(4,2)
r3 = somar(4)
print(f'{r1}, {r2} e {r3}')

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print('a dentro vale',a)
    print('b dentro vale', b)
    print('c dentro vale', c)

a = 5
teste(a)
print('a fora vale',a)
