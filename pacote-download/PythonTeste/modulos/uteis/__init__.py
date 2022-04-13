def leiaFloat():
    try:
        n = input('Digite um número: ')
    except Exception as erro:
        print('Infelizmente tivemos um problema... :(')
    else:
        print('Você digitou o número',n)