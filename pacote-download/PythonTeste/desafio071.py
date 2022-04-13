print('----------------')
print('CAIXA ELETRÔNICO')
print('----------------')

cd = x = 1
sc = 0
print('\n\033[4;33mNotas disponíveis: [R$50,00] [R$20,00] [R$10,00] [R$1,00]\033[m')
v = int(input('\nDigite o valor inteiro que você deseja sacar: R$'))
while True:
    cd = v // x % 10
    if cd == 0:
        break
    else:
        if x == 1:
            print(cd,'nota(s) de R$1,00')
        elif x == 10:
            if cd % 2 == 0:
                print(int(cd/2), 'nota(s) de R$20,00')
            elif (cd - 1) % 2 == 0 and cd % 5 != 0:
                print('1 nota(s) de R$10,00')
                print(int((cd - 1) / 2), 'nota(s) de R$20,00')
            elif cd % 5 == 0:
                sc = cd/5
            else:
                print(cd, 'nota(s) de R$10,00')
        else:
            sc += (cd/5)*(x/10)
    x = x * 10
if sc != 0:
    print(int(sc), 'nota(s) de R$50,00')


