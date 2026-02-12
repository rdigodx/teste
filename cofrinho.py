
cofrinho = []

while True: 
    dinheiro = float(input("Digite o valor que deseja guardar no cofrinho: "))

    if dinheiro == 0:
        break

    cofrinho.append(dinheiro)
    


entrada = len(cofrinho)

print(f"Quantidade inserida: {entrada}")    
print(f"Total guardado: R$ {sum(cofrinho)}")