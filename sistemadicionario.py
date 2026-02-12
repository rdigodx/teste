print()
usuario = input("Digite seu login:")
print()
senha = input("Digite sua senha:")
print()

credenciaisRecebidas = {
    'nome': usuario,
    'senha': senha
}

credenciaisCorretas = {
    'nome': 'rodrigo',
    'senha': 'senha'
}

if credenciaisRecebidas['nome'] == credenciaisCorretas['nome']  and credenciaisRecebidas['senha'] == credenciaisCorretas['senha']:
    print("Login Bem-sucedido")
else:
    print("Usuário ou senha incorretos")