numero_limite = input("ingrese un numero entero positivo:")
impares = []

for numero in range(1, int(numero_limite)+1):
    if numero % 2 == 1:
        impares.append(numero)

print(f"Los números impares hasta {numero_limite} son: {impares}")