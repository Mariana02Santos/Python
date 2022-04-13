for c in range(1,5):
    p = float(input('Peso da {}ª pessoa: '.format(c)))
    if c==1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print('Maior peso: {:.1f}'.format(maior))
print('Menor peso: {:.1f}'.format(menor))
