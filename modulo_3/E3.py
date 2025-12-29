string = "programacao"
vogais = "aeiou"
contador = 0

for letra in string:
    if letra in vogais:
        contador += 1

print(f"A string '{string}' tem {contador} vogais")