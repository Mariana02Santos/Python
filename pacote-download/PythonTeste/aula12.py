n = input('Qual é o seu nome? ')
if n == 'Mariana':
    print('Seu nome é muito bonito!')
elif n == 'Maria' or n == 'Pedro' or n == 'Paulo':
    print('Seu nome é bem comum no Brasil.')
else:
    print('Seu nome é bem normal...')
print('Tenha um bom dia, \033[33m{}\033[33m!'.format(n))
