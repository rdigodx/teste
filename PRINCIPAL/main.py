from perfil import usuario
from perfil import validacao

nome = input("\nDigite seu nome: ").upper()

try:
    idade = int(input("Digite sua idade: "))

    if validacao.idade_valida(idade):
        perfil = usuario.criar_perfil(nome, idade)
        print("\nPERFIL CRIADO:")
        print(f"Nome: {perfil['nome']}")
        print(f"Idade: {perfil['idade']}\n")
    else:
        print("Acesso negado! Você não tem permissão para criar um perfil.")

except ValueError:
    print("\nDIGITE APENAS NÚMERO!")





