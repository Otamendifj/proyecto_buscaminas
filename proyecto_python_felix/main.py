from tablero2 import Tablero
from casilla2 import Casilla
import requests
def api (endpoint, elemento, elemento2= None):
    
    #se hcae el request a la base de datos
    response = requests.get (endpoint)
    
    #se transforma esa respuesta en un diccionario 
    dictionary = dict(response.json ())
    
    #se retorna el diccionario
    if elemento2 == None:
        return dictionary['global'][elemento]
    else:
        return dictionary["global"][elemento][elemento2]

medida_tablero = api("https://github.com/Algoritmos-y-Programacion/api-proyecto/raw/refs/heads/main/config.json", "board_size")

fila = medida_tablero[0]
columna = medida_tablero[1]

tamano_tablero = fila*columna

print("Bienvenido a Buscaminas, que dificultad deseas jugar?")
dificultad = input("1. Facil \n2.Medio \n3.Dificil \n4.Imposible \n-->")

while True:
    if dificultad == "1":
            cantidad_minas =int(tamano_tablero*api("https://github.com/Algoritmos-y-Programacion/api-proyecto/raw/refs/heads/main/config.json", "quantity_of_mines", "easy"))
            break
    elif dificultad == "2":
            cantidad_minas = int(tamano_tablero*api("https://github.com/Algoritmos-y-Programacion/api-proyecto/raw/refs/heads/main/config.json", "quantity_of_mines", "medium"))
            break
    elif dificultad == "3":
            cantidad_minas = int(tamano_tablero*api("https://github.com/Algoritmos-y-Programacion/api-proyecto/raw/refs/heads/main/config.json", "quantity_of_mines", "hard"))
            break
    elif dificultad == "4":
            cantidad_minas = int(tamano_tablero*api("https://github.com/Algoritmos-y-Programacion/api-proyecto/raw/refs/heads/main/config.json", "quantity_of_mines", "impossible"))
            break
    else:
       print("Error, Intente una opcion valida")


for fila in range(6):
    for columna in range(6):
        if fila == 0 and columna == 0:  # Esquina superior izquierda
            print(" ", end=" ")
        elif fila == 0:  # Encabezado de columnas (números)
            print(columna, end=" ")
        elif columna == 0:  # Números de filas
            print(fila, end=" ")
        else:  # Contenido del tablero
            print("■", end=" ")
    print()  # Salto de línea al final de cada fila
