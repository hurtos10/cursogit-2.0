import requests

def verificar_pagina(url):
  """
  Función para verificar si una página está arriba y funcionando.

  Parámetros:
    url (str): La URL de la página que se quiere verificar.

  Retorno:
    bool: True si la página está arriba y funcionando, False en caso contrario.
  """
  try:
    # Hacemos una solicitud a la página
    respuesta = requests.get(url)

    # Si el código de estado es 200, la página está arriba y funcionando
    if respuesta.status_code == 200:
      return True

    # Si el código de estado no es 200, la página no está arriba y funcionando
    else:
      return False

  except Exception as e:
    # Si hay una excepción, la página no está arriba y funcionando
    print(f"Error al verificar la página: {e}")
    return False

# Ejemplo de uso
url = "https://www.google.com"

if verificar_pagina(url):
  print("La página está arriba y funcionando")
else:
  print("La página no está arriba y funcionando")