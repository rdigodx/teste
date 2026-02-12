peso = float(input("Qual seu peso?"))
altura = float(input("Qual sua altura?"))

def imc_pessoa(peso, altura):
    imc = peso / (altura ** 2) 
    return imc

resultado = imc_pessoa(peso, altura)

peso_ideal = 18.5 >= resultado <= 24.9


print(f"O resultado do IMC é: {resultado}")
print(f"você está com o peso ideal?{peso_ideal}")

