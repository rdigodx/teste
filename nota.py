
nota = float(input("QUAL SUA NOTA DE 0 A 10: "))

while 0 <  nota > 10:
    print("Nota Inválida! Tente novamente.")
    nota = float(input("QUAL SUA NOTA DE 0 A 10: "))

print(f"Nota {nota} registrada com sucesso!")
