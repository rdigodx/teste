numero = float(input("Digite o valor que deseja:"))
desconto = float(input("Quantos porcento de desconto deseja?"))

def sistema_desconto(numero, desconto):
    return numero * desconto / 100
    


resultado = sistema_desconto(numero, desconto)

print(f"valor com o desconto: {resultado}")
