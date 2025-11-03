pan= 3.49
numb= input("numero de barras de pan viejo vendidas: ")
cantidad= int(numb)*pan
descuento= float(cantidad)*0.60
final= int(cantidad)-float(descuento)
print(f"""el costo total de las barras de pan seria de {cantidad}
se le aplicara un descuento de {descuento} (60%) por no ser fresco
el costo final seria {final}""")
input()
