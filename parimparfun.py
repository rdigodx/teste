numero = float(input("DIGITE UM NÚMERO:"))

def verificar_par(numero):
    if numero % 2:
        return "Impar"
    else:
        return "Par"

resultado = verificar_par(numero)

print(f"{resultado}")
