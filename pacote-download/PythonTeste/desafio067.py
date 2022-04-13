print('---=---')
print('\033[1;33mTABUADA\033[m')
print('---=---')
while True:
    n = int(input('\nDigite um valor: '))
    if n < 0:
        break
    print('Digite um valor negativo caso queira parar o programa')
    for c in range(0,11):
        print(f'{n} x {c} = \033[33m{n*c}\033[m')
