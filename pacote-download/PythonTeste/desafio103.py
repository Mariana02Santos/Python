def ficha(n,g):
    '''if g == '':
        g = '0'''
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if n == '':
        n = '<desconhecido>'
    print(f'O jogador {n} fez {g} gols.')

nome = input('Nome do jogador: ').strip()
gol = input('Nº de gols: ')
ficha(nome,gol)
