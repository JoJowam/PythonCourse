data = input('Digite algo: ')
print("O tipo primitivo desse dado é: ", type(data))
print("Só tem espaços? ", data.isspace())
print("É um número? ", data.isnumeric())
print("É alfabético? ", data.isalpha())
print("É alfanumérico? ", data.isalnum())
print("Está em maiúsculas? ", data.isupper())

print("Está capitalizada? ", data.istitle())

print("Está em minúsculas? ", data.islower())