from datetime import date
s1 = 0
s2 = 0
aa = date.today().year
for c in range(1,8):
    d = int(input('Digite a data de nascimento da {}ª pessoa: '.format(c)))
    if aa-d >= 18:
        s1 += 1
    else:
        s2 += 1
print('Maiores de idade:',s1,'\nMenores de idade:',s2)

