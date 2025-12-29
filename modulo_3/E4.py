nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
notas = []

for i in range(1,4):
    while True:
        nota = float(input(f"Informe a {i} nota: "))
        notas.append(nota)
        break

media = sum(notas) / len(notas)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

print(media)