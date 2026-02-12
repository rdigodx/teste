numero = int(input("DIGITE UM NUMERO INTEIRO?"))

calculo = numero % 2

resultado_par = calculo == 0
print(f" È um numero par :{resultado_par}")

resultado_impar = calculo != 0
print(f" È um numero impar :{resultado_impar}")