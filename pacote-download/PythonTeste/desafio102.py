def fat(n,show):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: [opcional] Mostrar ou não a conta.
    :return: O valor Fatorial de um número n.
    """
    s = []
    f = 1
    while n >= 1:
        s.append(n)
        f *= n
        n -= 1
    s.append(f)
    print(f'{x}! = {f}')
    if show == True:
        for c in range(0,len(s)-2):
            print(f'{s[c]} X',end=' ')
        print(s[len(s)-2],end=' = ')
        print(s[len(s)-1])

x = int(input('Digite um valor: '))
y = input(f'[S/N] Quer ver a conta do fatorial de {x}? ').strip().lower()[0]
while y not in 'ns':
    y = input(f'Resposta inválida. [S/N] Quer ver a conta do fatorial de {x}? ').strip().lower()[0]
if y == 's':
    y = True
else:
    y = False
fat(x,show=y)


