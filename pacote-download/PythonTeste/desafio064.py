s = 0
q = 0
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    print('\033[4;42m[999] Finalizar o programa\033[m')
    if n != 999:
        s += n
        q += 1
print('Quantidade de números digitados (excetuando 999):',q)
print('Soma dos números digitados (excetuando 999):',s)
