def busqueda_burbuja(lista, elemento):
  """
  Función para realizar una búsqueda por burbuja en una lista.

  Parámetros:
    lista (list): La lista en la que se realiza la búsqueda.
    elemento (any): El elemento que se busca en la lista.

  Retorno:
    int: La posición del elemento en la lista si se encuentra, o -1 si no se encuentra.
  """

  n = len(lista)
  encontrado = False
  i = 0

  while i < n and not encontrado:
    if lista[i] == elemento:
      encontrado = True
      posicion = i
    else:
      i += 1

  if encontrado:
    return posicion
  else:
    return -1


def ordenamiento_burbuja(lista):
  """
  Función para realizar un ordenamiento por burbuja en una lista.

  Parámetros:
    lista (list): La lista que se ordena.

  Retorno:
    list: La lista ordenada.
  """

  n = len(lista)

  for i in range(n - 1):
    for j in range(n - i - 1):
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]

  return lista


# Ejemplo de uso

lista = [5, 2, 4, 6, 1, 3]

# Búsqueda
elemento = 4
posicion = busqueda_burbuja(lista, elemento)

if posicion == -1:
  print("El elemento {} no se encuentra en la lista.".format(elemento))
else:
  print("El elemento {} se encuentra en la posición {} de la lista.".format(elemento, posicion))

# Ordenamiento
lista_ordenada = ordenamiento_burbuja(lista)

print("Lista ordenada:", lista_ordenada)