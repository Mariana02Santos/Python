frase = 'Curso em Video Python'
print(frase[3:13:2])
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print(frase.find('curso'))
print('Curso' in frase)
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase.split()
print(frase.split())
dividido = frase.split()
print(dividido[2][3])
print('-'.join(dividido))
print(frase.upper().count('O'))

print('\n')

frase2 = '   Aprenda Python  '
print(frase2.strip())
print(frase2.rstrip()) #right
print(frase2.lstrip()) #left

print("""On disait dans le livre : Les serpents boas avalent leur
proie tout entière, sans la mâcher. Ensuite ils ne peuvent plus
bouger et ils dorment pendant les six mois de leur digestion.""")






