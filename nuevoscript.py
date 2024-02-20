import random

# Generar lista de 100 números aleatorios
numeros = [random.randint(1, 1000) for i in range(100)]

# Lista de letras
letrasx = list("qwertyuiop")

# Lista de letras
letras1 = list("aeiou")

# Concatenar letra aleatoria a cada número
numeros_letras = []
for numero in numeros:
  letra_aleatoria = random.choice(letrasx)
  numero_letra = str(numero) + letra_aleatoria
  numeros_letras.append(numero_letra)

  # Concatenar letra aleatoria a cada número
numeros_letras2 = []
for numerox in numeros:
  letra_aleatoria = random.choice(letras1)
  numero_letra = str(numero) + letra_aleatoria
  numeros_letras.append(numero_letra)


# Concatenar letra aleatoria a cada número
numeros_letrasx = []
for numero in numeros:
  letra_aleatoriax = random.choice(letrasx)
  numero_letrax = str(numero) + letra_aleatoria
  numeros_letras.append(numero_letra)

# Imprimir lista de números con letras
print("Lista de números con letras:")
print(", ".join(numeros_letras))
