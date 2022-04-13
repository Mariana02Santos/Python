from datetime import date
c = {'limpa':'\033[m','verdet':'\033[1;32m','verdef':'\033[42m'}
print('\033[1;32m-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[42mALISTAMENTO MILITAR\033[m')
print('\033[1;32m-=-=-=-=-=-=-=-=-=-\033[m')
a = int(input('Informe seu ano de nascimento: '))
aa = date.today().year
x = 'Serviço Militar'
if aa - a < 18:
    print('Você ainda irá se alistar no {}{}{}!'.format(c['verdet'],x,c['limpa']))
elif aa - a == 18:
    print('É hora de você se alistar no {}{}{}!'.format(c['verdet'],x,c['limpa']))
else:
    print('Você deveria ter se alistado no {}{}{} há'.format(c['verdet'],x,c['limpa']),aa - a - 18,'ano(s)!')



