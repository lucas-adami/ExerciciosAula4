degrau = int(input("Insira a altura do degrau em cm: "))
altura_escada = float(input("Insira a altura que voce vai subir (em metros): ")) * 100

quantia_degraus = altura_escada / degrau

print(f"Para subir a altura desejada voce vai precisar subir {quantia_degraus:2}")