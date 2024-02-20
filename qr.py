#Script de Python para generar un código QR a partir de un string de entrada
#Python
import qrcode

# Función para generar un código QR a partir de un string
def generar_qr(texto):
  # Crear un objeto QRCode
  qr = qrcode.QRCode()

  # Agregar el texto al código QR
  qr.add_data(texto)

  # Generar la imagen del código QR
  qr.make_image()

  # Guardar la imagen del código QR en un archivo
  qr.save("codigo_qr.png")

# Obtener el string de entrada del usuario
texto = input("Introduzca el texto para el código QR: ")

# Generar el código QR
generar_qr(texto)

# Mostrar un mensaje de éxito
print("¡Código QR generado exitosamente!")