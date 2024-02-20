# Este script solicita al user un número y verifies si es par o impar.

# Solicitar al user un número
numero = int(input("Ingresa un número: "))

# Verificar si el número es par o impar
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")