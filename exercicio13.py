salario = float(input("Insira o valor do salario: "))
consumo_quilowatt = float(input("Insira a quantia de qwt consumidos por mês na residencia: "))

valor_kwt = salario / 8
consumo_mes = consumo_quilowatt * valor_kwt
consumo_desconto = consumo_mes * 0.85

print(f"O valor em reais pago por kwh é: R${valor_kwt:.2f}")
print(f"O valor em reais pago neste mês é: R${consumo_mes:.2f}")
print(f"O valor em reais pago neste mês com o desconto é: R${consumo_desconto:.2f}")