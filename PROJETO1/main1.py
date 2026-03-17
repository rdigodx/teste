from pathlib import Path

acesso = Path("acesso.log")

with open(acesso, "r", encoding="utf-8") as leitura:
    for linha in leitura:
        if "ERROR" in linha or "INFO" in linha or "WARNING" in linha:
            print(linha)

