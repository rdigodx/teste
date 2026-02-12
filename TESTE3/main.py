from meu_pacote import formatador
from meu_pacote import numeros

texto = input("DIGITE UM TEXTO:")
numero = int(input("DIGITE UM NÚMERO PARA VERIFICAR SE É IMPAR OU PAR:"))

par_impar = numeros.par_impar(numero)

formatador.caixa_alta(texto)
print(f"Seu número é: {par_impar}")