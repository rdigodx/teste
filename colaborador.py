salario = float(input("Digite seu salário: "))

if salario <= 279:
    aumento = 0.20
elif 280 <= salario <= 699:
    aumento = 0.15
elif 700 <= salario <= 1499:
    aumento = 0.10
else:
    aumento = 0.05

valor_aumento = salario * aumento
salario_reajustado = salario + valor_aumento

print(f"Seu salário atual: R$ {salario}")
print(f"Percentual de aumento aplicado: {aumento*100}")
print(f"Valor do aumento: R$ {valor_aumento}")
print(f"Novo salário: R$ {salario_reajustado}")
