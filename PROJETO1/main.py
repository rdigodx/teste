from pathlib import Path

contador = 0

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

caminho_arquivo = Path("mensagem.txt")

caminho_arquivo.touch(exist_ok=True)


with caminho_arquivo.open('w', encoding='utf-8') as caminho_final:
    caminho_final.write(                                                                                                                                                          
                    "Ei! Acabei de ver uma nuvem"
                    )

with caminho_arquivo.open('r', encoding='utf-8') as leitura:
    texto = leitura.read().lower()

for letra in texto:
    if letra in alfabeto:
        contador += 1

print(contador)

