from ex115.lib.Interface import *
while True:
    resposta = menu(['Cadastrar Cliente','Ver Clientes Cadastrados','Sair do Sistema'])
    if resposta == 1:
        cab('1')
    elif resposta == 2:
        cab('2')
    elif resposta == 3:
        cab('Saindo do Sistema... Até logo!')
    else:
        print('\033[1;31mERRO! Digite uma opção válida.\033[m')

