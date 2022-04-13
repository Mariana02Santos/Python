r = 'o'
l = []
while r == 'o':
    n = int(input('Entrer une valeur: '))
    if n not in l:
        l.append(n)
    #if l.count(n) > 1:
    #    l.remove(n)
    r = input('[O/N] Souhaitez-vous continuer? ').strip().lower()[0]
    while r not in 'no':
        r = input('Réponse invalide. Souhaitez-vous continuer? ').strip().lower()[0]
l.sort()
print('Liste:',l)



