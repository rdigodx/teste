import random

placar = []

def funcao_listar():
    if not placar:
        print("\nVocê não jogou nenhuma partida!\n")
        return

    print("\nRESUMO DAS PARTIDAS:")
    print("| Partida | Tentativas | Pontos |")
    for p in placar:
        print(f"|   {p['partida']}     |     {p['tentativas']}      |   {p['pontos']}    |")

def numero_aleatorio():
    return random.randint(1, 100)

def dica(numero):
    if 1 <= numero <= 10:
        print("Dica: o número está entre 1 e 10")
    elif 11 <= numero <= 20:
        print("Dica: o número está entre 11 e 20")
    elif 21 <= numero <= 30:
        print("Dica: o número está entre 21 e 30")
    elif 31 <= numero <= 40:
        print("Dica: o número está entre 31 e 40")
    elif 41 <= numero <= 50:
        print("Dica: o número está entre 41 e 50")
    elif 51 <= numero <= 60:
        print("Dica: o número está entre 51 e 60")
    elif 61 <= numero <= 70:
        print("Dica: o número está entre 61 e 70")
    elif 71 <= numero <= 80:
        print("Dica: o número está entre 71 e 80")
    elif 81 <= numero <= 90:
        print("Dica: o número está entre 81 e 90")
    else:
        print("Dica: o número está entre 91 e 100")


print("\n-------------------------------------")
print("- BEM-VINDO AO JOGO DE ADIVINHAÇÃO -")
print("-------------------------------------")

numero_partida = 1

while True:
    try:
        menu = int(input(
            "\nEscolha uma das opções:\n"
            "1. JOGAR\n"
            "2. LISTAR PARTIDAS\n"
            "3. SAIR\n"
        ))
    except ValueError:
        print("\nDIGITE APENAS NÚMERO!")
        continue

    match menu:
        case 1:
            numero_secreto = numero_aleatorio()
            tentativa = 1
            pontos = 0
            acertou = False

            while tentativa <= 10:
                try:
                    numero = int(input(f"Tentativa {tentativa} - Digite um número de 1 a 100: "))
                except ValueError:
                    print("Digite apenas números!")
                    continue

                if numero == numero_secreto:
                    pontos = 100 - (tentativa - 1) * 10
                    if pontos < 10:
                        pontos = 10
                    print(f"\n🎉 Parabéns! Você acertou e fez {pontos} pontos!\n")
                    acertou = True
                    break
                else:
                    print("\nVocê errou! Tente novamente.")
                    dica(numero_secreto)

                tentativa += 1

            if not acertou:
                print(f"\n😢 Você perdeu! O número era {numero_secreto}\n")

            placar.append({
                'partida': numero_partida,
                'tentativas': tentativa if acertou else 10,
                'pontos': pontos
            })

            numero_partida += 1

        case 2:
            funcao_listar()

        case 3:
            print("\nSaindo...")
            break

        case _:
            print("\nOpção inválida! Digite 1, 2 ou 3.")
