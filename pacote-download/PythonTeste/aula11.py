#   CORES
#   \033[0;33;44m
#Obs: o 0 pode ser omitido

#   Style             Text        Back
#   0  None            30  Blanc   40
#   1  Bold (Negrito)  31  Rouge   41
#   4  Underline       32  Vert    42
#   7  Negative        33  Jaune   43
#                      34  Bleu    44
#                      35  Rose    45
#                      36  Cyan    46
#                      37  Gris    47

#   TESTE
print('\033[mOlá, mundo!\033[m') #padrao
print('\033[4;33;45mOlá, mundo!\033[m')
print('\033[1;34;43mOlá, mundo!\033[m')

a = 2
b = 3
print('Os valores são \033[4;35m{}\033[m e \033[4;36m{}\033[m'.format(a,b))

cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}
nome = 'Mariana'
print('Prazer em te conhecer, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpa']))
