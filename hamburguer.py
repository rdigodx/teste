list = []

while True:
    voto = float(input("Vote entre Hambúrguer ou Pizza:\n"
    "1.Pizza\n"
    "2.Hambúrguer\n"
    "3.Sair\n"
    "-"))

    if voto == 3:
        break

    list.append(voto)

print(f"Quantidade de votos de cada:\n"
    f"Pizza:{list.count(1)}\n"
    f"Hambúguer:{list.count(2)} ")
    
    
