nome = 'Maria'
idade = 15
salario = 1400.50
print(f'A {nome:<^20} tem {idade} anos e recebe R${salario:.2f}')

s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(s)

