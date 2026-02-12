raio = float(input("DIGITE O VALOR DO RAIO:"))

def calculo_area(raio):
    pi = 3.14
    area = pi * (raio ** 2)
    return area

resultado = calculo_area(raio)

print(F"O RESULTADO DO CALCULO DA AREA DE UM CIRCULO É: {resultado}")