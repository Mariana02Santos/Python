from emoji import emojize
from random import randint

c = {'limpa':'\033[m','cinza':'\033[1;37m','vermelho':'\033[1;31m','branco':'\033[1;30m'}
print('{}Pedra {}Papel {}Tesoura'.format(c['cinza'],c['branco'],c['vermelho']))
print(emojize('\033[33m:raised_fist:\033[m    '),emojize(':hand_with_fingers_splayed:    '),emojize(':victory_hand:'))

x = randint(1,3)
if x==1:
    x = emojize('\033[33m:raised_fist:\033[m')
elif x==2:
    x = emojize(':hand_with_fingers_splayed:')
elif x==3:
    x = emojize(':victory_hand:')

print('{}Pedra{} [ 1 ]\n{}Papel{} [ 2 ]\n{}Tesoura{} [ 3 ]'.format(c['cinza'],c['limpa'],c['branco'],c['limpa'],c['vermelho'],c['limpa']))

v = int(input('Escolha uma opção (1/2/3): '))
if v==1:
    v = emojize('\033[33m:raised_fist:\033[m')
elif v==2:
    v = emojize(':hand_with_fingers_splayed:')
elif v==3:
    v = emojize(':victory_hand:')
else:
    print('Opção {}INVÁLIDA{}. Tente novamente.'.format(c['vermelho'],c['limpa']))

print(v,' {}VS{}  '.format(c['vermelho'],c['limpa']),x)
if (v==emojize('\033[33m:raised_fist:\033[m') and x==emojize(':victory_hand:')) or (v==emojize(':hand_with_fingers_splayed:') and x==emojize('\033[33m:raised_fist:\033[m')) or (v==emojize(':victory_hand:') and x == emojize(':hand_with_fingers_splayed:')):
    print('Você \033[1;34mGANHOU{}!'.format(c['limpa']))
elif v == x:
    print('\033[1;33mEMPATE{}'.format(c['limpa']))
else:
    print('Você {}PERDEU{}!'.format(c['vermelho'],c['limpa']))


#print(emojize(':page_facing_up:'))
#print(emojize(':scissors:'))
#print(emojize(':curling_stone:'))
