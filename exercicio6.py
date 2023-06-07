salario = float(input("Insira o valor do seu salário: "))
aumento = float(input("Insira o valor do aumento do salario: ")) / 100
novo_salario = salario * (aumento + 1)
print(f"O valor do seu novo salario é de {novo_salario:2}")