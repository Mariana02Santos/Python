cor = {'limpa':'\033[m','rosat':'\033[1;35m','rosaf':'\033[1;45m'}
print('{}<><><><><><><><><>{}'.format(cor['rosaf'],cor['limpa']))
print('{}COMPRA DE PRODUTOS{}'.format(cor['rosat'],cor['limpa']))
print('{}<><><><><><><><><>{}'.format(cor['rosaf'],cor['limpa']))

s = mm = menor = 0
c = 1
mbarato = '0'
while True:
    n = input('\nNome do produto: ')

    p = float(input('Preço do produto: R$'))
    s += p
    if p > 1000:
        mm += 1
    if c == 1:
        menor = p
        mbarato = n
    else:
        if p < menor:
            menor = p
            mbarato = n

    c += 1

    r = input('{}[N/S] Deseja continuar?{} '.format(cor['rosaf'],cor['limpa'])).strip().upper()[0]
    while r not in 'NS':
        r = input('{}Resposta inválida. [N/S] Deseja continuar?{} '.format(cor['rosat'],cor['limpa'])).strip().upper()[0]
    if r == 'N':
        break

print(f'\nValor total da compra: R${s:.2f}')
print('Número de produtos que custam mais que R$1000.00:',mm)
print('Produto mais barato:',mbarato)



