from datetime import date
a = int(input('Digite um ano e eu informarei se ele é bissexto ou não (Digite 0 para selecionar o ano atual): '))
if a == 0:
    a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(a, 'é um ano bissexto')
else:
    print(a, 'não é um ano bissexto')
