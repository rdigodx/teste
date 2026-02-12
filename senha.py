usuario = input("LOGIN:")
senha = input("SENHA:")

while senha == usuario:
    print("ERRO!, senha nãonpode ser igual nome de usuário")
    usuario = input("LOGIN:")
    senha = input("SENHA:")