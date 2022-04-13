v = input('Digite o seu sexo (F/M): ').upper().strip()[0]
while v not in 'MmFf':
    v = str(input('Resposta inválida. Tente novamente (F/M): ')).strip().upper()[0]
print('Sexo {} registrado com Sucesso.'.format(v))

