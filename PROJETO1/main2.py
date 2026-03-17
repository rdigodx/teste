from pathlib import Path

tarefa1 = input("Digite a tarefa 1:")
tarefa2 = input("Digite a tarefa 2:")
tarefa3 =  input("Digite a tarefa 3:")

arquivo = Path("tarefas.txt")

with open(arquivo, 'w', encoding='utf-8') as caminho_final:
    caminho_final.write(
                    f"{tarefa1}\n"
                    f"{tarefa2}\n"    
                    f"{tarefa3}\n"    
                        )