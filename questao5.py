# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada
# de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

string = 'Hello World'
reversed_string = string[::-1]

print(reversed_string)  # :)

#  _____Outro método______

reversed_string = ''
n = len(string) - 1

for i in range(n, -1, -1):
    reversed_string += string[i]

print(reversed_string)
