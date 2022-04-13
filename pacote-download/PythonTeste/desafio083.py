print('\033[1;33mVerificação de EXPRESSÃO com base no uso dos PARÊNTESES\033[m')
e = input('Digite uma expressão: ')
if ('(' or ')') not in e:
    print('Sua expressão está correta.')
else:
    if e.count('(') == e.count(')'):
        l = e.split('(')
        if ')' in l[len(l)-1] and ')' not in l[0]:
            print('Sua expressão está correta.')
        else:
            print('Sua expressão está incorreta.')
    else:
        print('Sua expressão está incorreta.')
