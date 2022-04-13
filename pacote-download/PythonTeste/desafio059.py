n1 = int(input('Digite o 1ª valor: '))
n2 = int(input('Digite o 2ª valor: '))
x = 10
while x != 5:
    x = int(input('\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa\n\033[33mEscolha uma dessas opções:\033[m '))
    if x == 1:
        print('A soma dos valores {} e {} é igual a {}'.format(n1,n2,n1+n2))
    if x == 2:
        print('A multiplicação dos valores {} e {} é igual a {}'.format(n1, n2, n1 * n2))
    if x == 3:
        if n1 > n2:
            print('Entre os valores {} e {}, o maior é o {}'.format(n1, n2, n1))
        else:
            print('Entre os valores {} e {}, o maior é o {}'.format(n1, n2, n2))
    if x == 4:
        n1 = int(input('Digite o 1ª valor: '))
        n2 = int(input('Digite o 2ª valor: '))

print('Bye bye')
