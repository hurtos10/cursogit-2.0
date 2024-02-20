'''
GENERADOR DE CONTRASEÑAS SEGURAS
'''

import secrets
import string

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters  + string.digits + string.punctuation
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena

# Solicitar al usuario la longitud deseada para la contraseña
longitud_contraseña = int(input("Ingrese la longitud deseada para la contraseña: "))
if longitud_contraseña < 8:
    print('La longitud de la contraseña es muy chica.')
    exit()

# Generar la contraseña y mostrarla
contraseña_generada = generar_contrasena(longitud_contraseña)
print(f"Contraseña generada: {contraseña_generada}")

