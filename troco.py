dinheirototal = 50

gasto1 = float(input("DIGITE O VALOR DA PRIMEIRA COMPRA?"))
gasto2 = float(input("DIGITE O VALOR DA SEGUNDA COMPRA?"))
gasto3 = float(input("DIGITE O VALOR DA TERCEIRA COMPRA?"))
gastoadcional = []

while True:
    resposta = input("VAI FAZER MAIS COMPRAS? Digite 'S' para sim ou 'N' para não: ").strip().upper()

    if resposta == 'N':
        break
    elif resposta == 'S':
        novo_gasto = float(input("DIGITE O VALOR DA NOVA COMPRA? R$"))
        gastoadcional.append(novo_gasto)
    else:
        print("Resposta inválida. Digite apenas 'S' ou 'N'.")

resultado = dinheirototal - gasto1 - gasto2 - gasto3 - sum(gastoadcional)

if resultado == 0:
    print("VOCÊ NÃO TEM TROCO!")
else:
    print(f"Meu troco foi de R${resultado}")
