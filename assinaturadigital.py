from datetime import datetime
import locale 

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def assinatura(nome):
    data_assinatura = datetime.now()
    print(data_assinatura.strftime(f"Assinatura gerada por {nome} em %d de %B de %Y às %H:%M"))


nome = input("Digite seu nome para realizar a assinatura:").upper()

assinatura(nome)