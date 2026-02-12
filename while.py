
lista = []

while len(lista) < 5:
    nome = input("Digite um nome: ")
    lista.append(nome) 

print("Limite atingido!")
print(f"Lista de nomes: {lista}")

print("Lista de nomes:")
for nome in lista:
    print(nome)




