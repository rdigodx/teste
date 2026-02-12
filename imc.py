peso = float(input("Qual seu peso?"))
altura = float(input("Qual sua altura?"))

imc = peso / (altura ** 2)
print(f"Seu imc: {imc:.2f}")

peso_ideal = 18.5 >= imc <= 24.9
print(f"você está com o peso ideal?{peso_ideal}")

