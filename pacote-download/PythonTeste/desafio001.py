x = input('Digite algo: ')
print('O que foi digitado é um número:' , x.isnumeric())
print('O que foi digitado é alfanumérico:' , x.isalnum())
print('O que foi digitado é alfabético:' , x.isalpha())
print(x.isascii())
print(x.isdigit())
print('O que foi digitado é um valor decimal:' , x.isdecimal())
print(x.isidentifier())
print('O que foi digitado possui apenas letras minúsculas:' , x.islower())
print(x.isprintable())
print('O que foi digitado possui apenas espaços:' , x.isspace())
print('O que foi digitado é capitalizado:' , x.istitle())
print('O que foi digitado possui apenas letras maiúsculas:' , x.isupper())
print(x.__init_subclass__())
print(type(x))



