print('-=-=-=-=-=-=-=-=-=-')
print('EMPRÉSTIMO BANCÁRIO')
print('-=-=-=-=-=-=-=-=-=-')
v = float(input('Valor da casa: '))
s = float(input('Salário do comprador: '))
a = int(input('Quantidade de anos nos quais o pagamento ocorrerá: '))
if v/(a*12) > 0.3*s:
    print('Empréstimo \033[1;31mNEGADO\033[m!')
else:
    print('Empréstimo \033[1;32mACEITO\033[m!')
print('-=-=-=-=-=-=-=-=-=-')

