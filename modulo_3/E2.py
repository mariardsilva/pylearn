numeros = []

for i in range(1,6):
    while True:
        num = float(input(f"Digite o {i} numero: "))
        numeros.append(num)
        break

media = sum(numeros) / len(numeros)
print(media)