from random import randint
print('\033[1;31m-=-=-=-=-=-=-=-=-\033[m')
print('   Ímpar \033[1;31mX\033[m Par')
print('\033[1;31m-=-=-=-=-=-=-=-=-\033[m')

s = 0

while True:
    x = input('[I/P] Ímpar ou Par? ').strip().upper()[0]
    while x not in 'IPÍ':
        x = input('Resposta inválida. Tente novamente [I/P]: ').strip().upper()[0]
    n = int(input('Escolha um número: '))
    c = randint(0,10)
    print('O comutador escolheu o número',c)
    print(f'{n} + {c} = {n+c}')
    if ((n+c)%2==0 and x=='P') or ((n+c)%2!=0 and (x=='I' or x=='Í')):
        print('Você \033[1;32mGANHOU\033[m!')
        s += 1
    else:
        print('Você \033[1;31mPERDEU\033[m!')
        break
print('Número de vitórias do jogador:',s)
