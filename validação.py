sexos = {"F": "Feminino", "M": "Masculino"}
estados = {"S": "Solteiro(a)", "C": "Casado(a)", "V": "Viúvo(a)", "D": "Divorciado(a)"}

nome = input("QUAL O SEU NOME:")

while len(nome) <= 4:
    print("VALOR INVÁLIDO!, nome deve ter mais que 4 caracteres")
    nome = input("QUAL O SEU NOME:")

idade = float(input("QUAL SUA IDADE:"))

while idade < 1 or idade > 27:
    print("valor invalido!, sua idade dever ser entre 1 e 27 anos")
    idade = float(input("QUAL SUA IDADE:"))

salario = float(input("DIGITE SEU SALÁRIO:"))

while salario <= 0:
    print("Valor inválido!, seu salário deve ser maior que 0.")
    salario = float(input("DIGITE SEU SALÁRIO:"))

sexo = input("QUAL SEU SEXO (F OU M):").upper()

while sexo != "F" and sexo != "M":
    print("Valor inválido! Digite F ou M")
    sexo = input("QUAL SEU SEXO (F OU M):").upper()

estadocivil = input("QUAL SEU ESTADO-CIVIL (S, C, V, D):").upper()

while estadocivil != "S" != "C" != "V" != "D":
    print("Estado civil inválido! Digite S, C, V ou D")
    estadocivil = input("QUAL SEU ESTADO-CIVIL (S, C, V, D):").upper()


print("CADASTRO CONCLUIDO COM SUCESSO!")
print(f"Nome:{nome}")
print(f"Idade:{idade}")
print(f"Salário:{salario}")
print(f"Sexo:{sexo}")
print(f"Estado civil:{estadocivil}")