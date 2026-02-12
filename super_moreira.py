carrinho = []
total = 0

print("=" * 60)
print("  BEM-VINDO AO SUPERMERCADO MOREIRA!  ")
print("=" * 60)

while True:
    if len(carrinho) > 5:
        break


    escolha = input("\nESCOLHA O ITEM (ou '0' para finalizar)::\n" 
    "1 - Arroz (5kg): R$ 32.90 \n"
    "2 - Feijão Carioca (1kg): R$ 7.80 \n"
    "3 - Café Moído (500g): R$ 19.50 \n"  
    "4 - Leite Integral (1L): R$ 5.90 \n"  
    "5 - Óleo de Soja (900ml): R$ 6.50 \n"
    "6 - Açúcar Refinado (1kg): R$ 4.20 \n"
    "7 - Pão de Forma: R$ 8.90 \n"
    "8 - Dúzia de Ovos: R$ 11.50 \n"
    "-")

    if escolha == "0":
        break
    elif escolha == "1":
        carrinho.append("Arroz (5kg)")
        total += 32.90
    elif escolha == "2":
        carrinho.append("Feijão Carioca (1kg)")
        total += 7.80
    elif escolha == "3":
        carrinho.append("Café Moído (500g)")
        total += 19.50
    elif escolha == "4":
        carrinho.append("Leite Integral (1L)")
        total += 5.90
    elif escolha == "5":
        carrinho.append("Óleo de Soja (900ml)")
        total += 6.50
    elif escolha == "6":
        carrinho.append("Açúcar Refinado (1kg)")
        total += 4.20
    elif escolha == "7":
        carrinho.append("Pão de Forma")
        total += 8.90
    elif escolha == "8":
        carrinho.append("Dúzia de Ovos")
        total += 11.50
    else:
        print("Opção inválida!")

print("ITENS NO CARRINHO:")
for escolha in carrinho:
    print(f" - {escolha}")

print(f"VALOR TOTAL DA COMPRA: {total}")




