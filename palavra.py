palavra = input("Digite uma palavra: ")
print(f"A primeira letra de '{palavra}' é {palavra[0]} é a ultima é {palavra[-1]}")

#

frase = input("DIGITE UMA FRASE:")
inicio = int(input("Informe o inicio do fatiamento:"))
final = int(input("Informe o final do fatiamento:"))
print(f"A frase fatida fica: {frase[inicio:final]}")

#


frase = input("Informe o que gostaria de fazer este ano:")
if "bomba" in frase:
    print("ALERTA TOTAL! QUER EXPLODIR")
else:
    print("Nenhuma ameaça detectada!")