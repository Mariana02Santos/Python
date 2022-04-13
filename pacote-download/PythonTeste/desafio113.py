def leiaFloat():
    while True:
        try:
            n = float(input('Digite um número: '))
        except:
            print('\033[1;31mERRO! Tente novamente\033[m')
        else:
            print('Você digitou o número',n)
            if type(n) == float or type(n) == int:
                break

x = leiaFloat()

