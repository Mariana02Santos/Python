tupla = ('un','deux','trois','quatre','cinq')
n = int(input('Choisissez un chiffres de 1 à 5: '))
while n < 1 or n > 5:
    n = int(input('Réponse invalide. Choisissez un chiffres de 1 à 5: '))
print('Vouz avez choisi le chiffres',tupla[n-1])
