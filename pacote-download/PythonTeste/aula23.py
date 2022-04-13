try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('Infelizmente tivemos um problema... :(')
    print(f'O problema encontrado foi {erro.__class__}')
except (ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou!')
else:
    print('Deu certo! :D')
    print(f'{a}/{b} = {r:.1f}')
finally:
    print('Volte sempre!')
