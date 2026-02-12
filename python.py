nome = "rodrigo";
idade = 20;
altura = 1.75;



calculo = 2025 - idade;

if idade >= 18:
    resultado = "Maior de idade"
else:
    resultado = "Menor de idade"

print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")
print(f"Nasci em {calculo} é sou {resultado}")

estudante = input("Você é estudante?[true/false]:")

if estudante == "true":
    print("Você é estudante!")
elif estudante == "false":
    print("Você não é estudante.")   