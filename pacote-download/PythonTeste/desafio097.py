def l(b):
    print('-'*(b+6))
def escreva(a):
    l(len(a))
    print('  ',a,'  ')
    l(len(a))

x = input('Escreva algo: ')
escreva(x)