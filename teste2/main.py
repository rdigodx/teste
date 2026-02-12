from matematica import dobro,metade
from mensagens import boas_vindas

nome = input("Digite seu nome:")
numero = int(input("Digite seu número:"))


boas_vindas(nome)
print(dobro(numero))
print(metade(numero))