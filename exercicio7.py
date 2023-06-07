deposito = float(input("Insira o valor do seu depositado: "))
taxa_juros = float(input("Insira o valor da taxa do juros: ")) / 100
rendimento = deposito * taxa_juros
rendimento_total = deposito * (taxa_juros + 1)

print(f"O valor que rendeu foi {rendimento:2} que somado ao seu deposito ficou {rendimento_total:2}")