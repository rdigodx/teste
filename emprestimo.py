valor_emprestimo = float(input("INFORME O VALOR DO EMPRÉSTIMO:"))

renda = float(input("INFORME SUA RENDA MENSAL:"))

parcela = float(input("INFORME A QUANTIDADE DE PARCELAS:"))

emprestimo = valor_emprestimo / parcela

calculo = renda * (30/100)

if emprestimo > calculo:
    print("Reprovado seu numero de parcelas excedeu 30%")
else: 
    print("Aprovado! parabens ")

