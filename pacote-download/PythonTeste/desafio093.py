d = {}
l = []
lt = []
lt2 = []
s = 0
while True:
    d.clear()
    d['Nome'] = input('Nome: ').upper()
    p = int(input('Número de partidas: '))
    l.clear()
    for c in range(0,p):
        l.append(int(input(f'Nº de gols partida {c+1}: ')))
        s += l[c]
    d['Aproveitamento'] = l[:]
    d['Nº total de gols'] = s
    s = 0
    lt.append(d.copy())
    del d['Aproveitamento']
    lt2.append(d.copy())
    r = input('[S/N] Deseja continuar? ').strip().upper()[0]
    while r not in 'SN':
        r = input('Resposta inválida. [S/N] Deseja continuar? ').strip().upper()[0]
    if r in 'N':
        break
print(f'\n{lt2}')
while True:
    r = input('\n[S/N] Gostaria de ver o aproveitamento de algum jogador? ').strip().upper()[0]
    while r not in 'SN':
        r = input('\nResposta inválida. [S/N] Gostaria de ver o aproveitamento de algum jogador? ').strip().upper()[0]
    if r in 'N':
        break
    else:
        x = input('Digite o nome do jogador: ').strip().upper()
        for c in lt:
            '''while x not in c['Nome']:
                x = input('Nome não encontrado. Digite o nome do jogador: ').strip().upper()'''
            if c['Nome'] == x:
                print(c['Aproveitamento'])



