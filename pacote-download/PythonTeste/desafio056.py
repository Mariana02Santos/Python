si = 0
sm = 0
maiori = 0
mvelho = '0'
for c in range(1,5):
    n = input('Nome da {}ª pessoa: '.format(c))
    i = int(input('Idade da {}ª pessoa: '.format(c)))
    s = input('Sexo da {}ª pessoa (F/M): '.format(c)).lower()
    if s=='f':
        if i < 20:
            sm += 1
    elif s=='m':
        if i > maiori:
            mvelho = n
    else:
        print('Resposta inválida. Tente novamente.')
    si += i
print('Média das idades:',si/4)
print('Nome do homem mais velho:',mvelho)
print('Número de mulheres com idade inferior a 20 anos:',sm)

