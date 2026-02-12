numero = int(input("DIGITE UM NUMERO: "))

resultado = 0

for i in range(1, 10 + 1):
    resultado = i * numero
    print(f'{i} x {numero} = {resultado}')