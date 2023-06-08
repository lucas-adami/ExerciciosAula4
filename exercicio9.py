from math import pi

diametro = float(input("Digite a medida do diametro do seu circulo: "))
raio = diametro / 2
area =  pi * (raio**2)
print(f"A área do circulo vai ser {area:2}")