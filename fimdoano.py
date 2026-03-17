from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

hoje = datetime.now()
fim_ano = datetime(2026,12,31)

dias_restantes = fim_ano - hoje
print(f"Faltam {dias_restantes.days} dias para acabar o ano.")
