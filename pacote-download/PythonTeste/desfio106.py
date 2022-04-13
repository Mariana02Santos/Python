def ajuda(com):
    print(f'\033[45m{help(com)}')

comando = ''
while True:
    comando = str(input('\033[44mFunção ou Biblioteca:'))
    if comando.upper() in 'FIM':
        break
    else:
        ajuda(comando)