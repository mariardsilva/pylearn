lista = [1, 2, 3, 4, 5, 6]
quadrados = [n * n for n in lista]
pares = [n for n in lista if n % 2 == 0]
maiores = [n for n in lista if n > 3]

print("Lista:",lista)
print("Quadrados:",quadrados)
print("Pares:",pares)
print("Maiores que 3:",maiores)