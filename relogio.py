from datetime import datetime

horario = datetime.now()

meio_dia = datetime.strptime("12:00", "%H:%M")

seis_tarde = datetime.strptime("18:00", "%H:%M")

if horario < meio_dia:
    print("Bom dia!")
elif meio_dia <= horario < seis_tarde:
    print("Boa tarde!")
else:
    print("Boa noite!")

