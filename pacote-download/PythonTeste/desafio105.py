def notas(*n,sit):
    r = '0'
    q = soma = maior = menor = 0
    d = {}
    while r not in 'n':
        n = float(input('Nota: '))
        q += 1
        soma += n
        if r == '0':
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
        r = input('Deseja continuar? ').strip().lower()[0]
        while r not in 'ns':
            r = input('Resposta inválida.[S/N] Deseja continuar? ').strip().lower()[0]
    m = soma/q
    d['Quantidade'] = q
    d['Média'] = m
    d['Maior'] = maior
    d['Menor'] = menor
    if m >= 7:
        d['Situação'] = 'BOA'
    if m < 7:
        d['Situação'] = 'RUIM'
    if sit == True:
        print(d)
    else:
        del d['Situação']
        print(d)

s = input('Deseja ver a situação da turma? ').strip().lower()[0]
while s not in 'ns':
    s = input('Resposta inválida.[S/N] Deseja continuar? ').strip().lower()[0]
if s in 's':
    s = True
else:
    s = False
notas(0,sit=s)

'''
min(n)
max(n)
'''

