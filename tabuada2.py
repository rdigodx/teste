num = float(input("Digite um número entre 1 e 10:"))

while 1 < num > 10:
    print("Esse número não está entre 1 e 10, tente novamente!")
    num = float(input("Digite um número entre 1 e 10:"))

for i in range(1, 10 + 1):
    resultado = i * num
    print(f'{i} x {num} = {resultado}')
