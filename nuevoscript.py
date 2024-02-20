import random

# Generar lista de 100 números aleatorios
numeros = [random.randint(1, 1000) for i in range(100)]

# Lista de letras
letras = list("zyxwvutsrqponmlkjihgfedcba")

# Lista de letras
letras1 = list("aeiou")

# Concatenar letra aleatoria a cada número
numeros_letras = []
for numero in numeros:
  letra_aleatoria = random.choice(letras)
  numero_letra = str(numero) + letra_aleatoria
  numeros_letras.append(numero_letra)

  # Concatenar letra aleatoria a cada número
numeros_letras2 = []
for numerox in numeros:
  letra_aleatoria = random.choice(letras1)
  numero_letra = str(numero) + letra_aleatoria
  numeros_letras.append(numero_letra)