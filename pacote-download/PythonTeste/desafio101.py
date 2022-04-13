from datetime import date
def voto(a):
    i = date.today().year - a
    if i >= 18 and i < 70:
        r = 'OBRIGATÓRIO'
    elif i >= 16 and i < 18 or i >= 70:
        r = 'FACULTATIVO'
    else:
        r = 'NEGADO'
    return r

x = int(input('Ano de Nascimento: '))
print('Situação Voto:',voto(x))
