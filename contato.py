lista = []

def funcao_buscar(contato_busca):
    for contato in lista:
        if contato['nome'] == contato_busca:
            print(
                "\nContato encontrado!"
                f"\nNome: {contato['nome']} | Telefone: {contato['telefone']}"
            )
            return
    print("\nContato não encontrado!")

def funcao_remover(contato_remove):
    for contato in lista:
        if contato['nome'] == contato_remove:
            lista.remove(contato)
            print("\nContato removido!")
            return
    print("\nContato não encontrado!")

def funcao_listar():
    if not lista:
        print("\nNenhum contato cadastrado!")
        return
    
    print("\nLista de contatos:")
    for contato in lista:
        print(f"Nome: {contato['nome']} | Telefone: {contato['telefone']}")

while True:
    try:
        opcao = int(input(
            "\nEscolha uma das opções abaixo:\n"
            "1. Adicionar contato\n"
            "2. Buscar contato\n"
            "3. Remover contato\n"
            "4. Listar contatos\n"
            "5. Sair\n"
            "- "
        ))

    except ValueError:
        print("\nDIGITE APENAS NÚMERO!")
        continue

    match opcao:
        case 1:
            nome = input("Digite o nome do contato:\n")
            telefone = input("Digite o telefone:\n")

            informacao = {
                'nome': nome,
                'telefone': telefone
            }

            lista.append(informacao)
            print("\nContato adicionado com sucesso!")

        case 2:
            contato_busca = input("Digite o nome do contato:\n")
            funcao_buscar(contato_busca)

        case 3:
            contato_remove = input("Digite o nome do contato:\n")
            funcao_remover(contato_remove)

        case 4:
            funcao_listar()

        case 5:
            print("\nSaindo...")
            break

        case _:
            print("\nOpção inválida! Digite um número entre 1 e 5.")


