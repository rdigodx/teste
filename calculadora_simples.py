numero1 = float(input("Digite o primeiro Número:"))
numero2 = float(input("Digite o segundo Número:"))


operacao = int(input(
    "Escolha uma operação:\n"
    "1 - SOMA\n"
    "2 - SUBTRAÇÃO\n"
    "3 - MULTIPLICAÇÃO\n"
    "4 - DIVISÃO\n"
))

if operacao == 1:
    resultado1 = numero1 + numero2     
    print(f"Resultado da soma:{resultado1}")

elif operacao == 2:
    resultado2 = numero1 - numero2
    print(f"Resultado da subtração:{resultado2}")

elif operacao == 3:
    resultado3 = numero1 * numero2
    print(f"Resultado da multiplicação:{resultado3}")

elif operacao == 4:    
    if numero2 != 0:
        resultado4 = numero1 / numero2
        print(f"Resultado da divisão:{resultado4}")
    else:
        print(f"Não é possível dividir por zero.")

else:
    print(f"Opção inválida!")
