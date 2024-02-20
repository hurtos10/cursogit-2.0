import requests
import datetime

# Función para obtener la hora actual
def obtener_hora_actual():
    return datetime.datetime.now().strftime("%H:%M:%S")

# Función para obtener el clima en Nueva York
def obtener_clima_newyork():
    # API Key de Weather API
    api_key = "YOUR_API_KEY"

    # URL de la API
    url = "https://api.openweathermap.org/data/2.5/weather?q=New%20York&appid={}".format(api_key)

    # Petición a la API
    respuesta = requests.get(url)

    # Decodificación de la respuesta en formato JSON
    datos = respuesta.json()

    # Temperatura actual
    temperatura = datos["main"]["temp"] - 273.15

    # Descripción del clima
    descripcion = datos["weather"][0]["description"]

    return "Temperatura: {:.2f}°C, Clima: {}".format(temperatura, descripcion)

# Obtención de la hora actual
hora_actual = obtener_hora_actual()

# Obtención del clima en Nueva York
clima_newyork = obtener_clima_newyork()

# Saludo y mensaje con la hora y el clima
print("¡Buenos días!")
print("Son las {} en Ciudad de México.".format(hora_actual))
print("El clima en Nueva York es: {}".format(clima_newyork))