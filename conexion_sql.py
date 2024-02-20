import pyodbc

# Configuración de la conexión
server = 'tu_servidor_sql'  # Cambia esto con la dirección de tu servidor SQL
database = 'tu_base_de_datos'  # Cambia esto con el nombre de tu base de datos
username = 'tu_usuario'  # Cambia esto con tu nombre de usuario
password = 'tu_contraseña'  # Cambia esto con tu contraseña

# Cadena de conexión
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Establecer la conexión
    connection = pyodbc.connect(connection_string)

    # Crear un cursor desde la conexión
    cursor = connection.cursor()

    # Ejemplo de consulta
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    print("Versión del servidor SQL Server:", row[0])

except Exception as e:
    print(f"Error de conexión: {str(e)}")

finally:
    # Cerrar la conexión al finalizar
    if 'connection' in locals():
        connection.close()
