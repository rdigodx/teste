from pathlib import Path
from datetime import datetime
import shutil

tipos_arquivos = ["txt", "pdf", "docx", "xlsx", "png", "jpg"]

logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

log_file = logs_dir / "log.txt"

arquivo_zip = Path("organizador.zip")
pasta_destino = Path("Organizador_de_pasta")
pasta_temp = Path("pasta_temporaria")

with log_file.open("w", encoding="utf-8") as log:
    if not pasta_destino.exists():
        pasta_destino.mkdir()
        log.write(f"[CRIADO] Pasta: {pasta_destino} | {datetime.now()}\n")

    if not pasta_temp.exists():
        pasta_temp.mkdir()
        log.write(f"[CRIADO] Pasta: {pasta_temp} | {datetime.now()}\n")

    for nome in tipos_arquivos:
        sub = pasta_destino / nome
        if not sub.exists():
            sub.mkdir()
            log.write(f"[CRIADO] Subpasta: {sub} | {datetime.now()}\n")

    shutil.unpack_archive(arquivo_zip, pasta_temp)
    log.write(f"[EXTRAÍDO] {arquivo_zip} -> {pasta_temp} | {datetime.now()}\n")

    for file in pasta_temp.rglob("*"):
        if file.is_file():
            extensao = file.suffix.lower().replace('.', '')

            if extensao in tipos_arquivos:
                destino = pasta_destino / extensao / file.name

                shutil.move(file, destino)
                log.write(f"[MOVIDO] {file.name} -> {destino} | {datetime.now()}\n")

    shutil.rmtree(pasta_temp)
    log.write(f"[REMOVIDO] Pasta: {pasta_temp} | {datetime.now()}\n")
