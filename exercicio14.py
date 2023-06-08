horario = float(input("Digite o horário, separando os minutos com '.': "))

hora = int(horario)
minutos = 100 * (horario - hora)

horario_minutos = hora * 60 + minutos

print(f"O horário convertido em minutos pode ser mostrado por: {horario_minutos} minutos.")
