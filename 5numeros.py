
#list = []
#
#while len(list) < 5:
#    numero = float(input("Digite um numero: "))
#    list.append(numero) 
#
#resultado = sum(list)
#
#print(f"Seu resutado da soma é: {resultado}")

list = []

for i in range(5):
    i = float(input("Digite um numero: "))
    list.append(i) 

resultado = sum(list)

print(f"Seu resutado da soma é: {resultado}")