v = float(input('Preço do produto: '))
print('\033[4;33mDinheiro/Cartão: Digite 0\033[m')
print('\033[4;33mCartão: Digite qualquer número excetuando 0\033[m')
f = int(input('Escolha uma forma de pagamento: '))
if f==0:
    print('Valor do produto com desconto: R${:.2f}'.format(v - v*0.1))
else:
    p = int(input('Informe o número de parcelas: '))
    if p==1:
        print('Valor do produto com desconto: R${:.2f}'.format(v - v*0.05))
    elif p==2:
        print('Valor do produto: R${:.2f}'.format(v))
    else:
        print('Valor do produto com juros: R${:.2f}'.format(v*(1.2)**p))
