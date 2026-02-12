nome = input("Digite seu nome:")
idade = input("Digite sua idade:")

pessoa = {
    'nome': nome,
    'idade': idade
}

print(f"Seu nome é {pessoa['nome']}, é você  tem {pessoa['idade']}")