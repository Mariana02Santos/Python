print('\033[33m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print(' Conversor de Bases Numéricas')
print('\033[33m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
n = int(input('Digite um valor inteiro: '))
print('\033[4;33mBinária [ 1 ]\nOctal [ 2 ]\nHexadecimal [ 3 ]\033[m')
c = int(input('Para qual base você quer converter esse número? '))
if c==1:
    print('{} convertido para BINÁRIO é {}'.format(n,bin(n)[2:]))
elif c==2:
    print('{} convertido para OCTAL é {}'.format(n,oct(n)[2:]))
elif c==3:
    print('{} convertido para HEXADECIMAL é {}'.format(n,hex(n)[2:]))
else:
    print('Opção Inválida. Tente Novamente.')
