
list = []


limite_list = float(input("Defina o limite de notas:"))

while len(list) < limite_list:
    nota1 = float(input("Digite a primeira nota: "))
    list.append(nota1) 

media = sum(list)  /2

print(f"Média: {media}")

if media == 10:
    print("APROVADO COM MAESTRIA!")
elif media >= 7:
    print("APROVADO!")
else:
    print("VOCÊ FOI REPROVADO.")



