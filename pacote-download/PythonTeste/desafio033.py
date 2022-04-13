n1 = int(input('Digite o 1º nº: '))
n2 = int(input('Digite o 2º nº: '))
n3 = int(input('Digite o 3º nº: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n3
if n2>n3 and n2>n1:
    maior = n2
if n1>n2 and n1>n3:
    maior = n1

print('Maior número:', maior)
print('Menor número:', menor)


#n1 = int(input('Digite o 1º nº: '))
#n2 = int(input('Digite o 2º nº: '))
#n3 = int(input('Digite o 3º nº: '))
#if n1 > n2 and n1 > n3:
#    print('Maior número:', n1)
#    if n2 > n3:
#        print('Menor número:', n3)
#    else:
#        print('Menor número:', n2)
#else:
#    if n2 > n3:
#        print('Maior número:', n2)
#        if n3 > n1:
#            print('Menor número:', n1)
#        else:
#            print('Menor número:', n3)
#    else:
#        print('Maior número:', n3)
#        if n2 > n1:
#            print('Menor número:', n1)
#        else:
#            print('Menor número:', n2)

