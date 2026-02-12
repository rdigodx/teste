nota1 = float(input("DIGITE A PRIMEIRA NOTA:"))
nota2 = float(input("DIGITE A SEGUNDA NOTA:"))

media = (nota1 + nota2) / 2

print("Sua média é:", media)

if media == 10:
    print("APROVADO COM MAESTRIA!")
elif media >= 7:
    print("APROVADO!")
else:
    print("VOCÊ FOI REPROVADO.")