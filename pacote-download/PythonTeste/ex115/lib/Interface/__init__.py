def l(tam=42):
    return '-'*tam
def cab(txt):
    print(l())
    print(txt.center(42))
    print(l())
def menu(lista):
    print(cab('MENU'))
    x = 1
    for c in lista:
        print(f'{x} - {c}')
        x += 1
    print(l())
    opc = leiaFloat('Sua opção: ')
