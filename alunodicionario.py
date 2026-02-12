aluno = input("Digite seu nome:")
print()
media = float(input("Digite sua Média:"))
print()

verificacao = {
    'aluno': aluno,
    'media': media
}

if verificacao['media'] >= 7:
    verificacao['situacao'] = 'APROVADO'
else:
    verificacao['situacao'] = 'REPROVADO'

print(f"O aluno {verificacao['aluno']}, teve média {verificacao['media']} e está {verificacao['situacao']}")


