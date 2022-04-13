def leiaFloat():
    n = input('Digite um número inteiro: ')
    while not(n.isnumeric()):
        print('\033[1;31mERRO. Escreva um número inteiro válido!\033[m')
        n = input('Digite um número inteiro: ')



