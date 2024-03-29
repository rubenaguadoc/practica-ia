import sqlite3 # Libreria de la BDD que vamos a usar.

# Devuelve la distancia con los vecinos de la estacion.
# Devuelve un diccionario <nodo, distancia>.
def getDistanciaTren(nodo):
    db = sqlite3.connect('metroDataBase.db')
    diccio = {}
    cursor = db.cursor()

    nodo = str(nodo)

    cursor.execute("SELECT DESTINO, DISTANCIA FROM tren WHERE ORIGEN = ?", (nodo,))
    for i in cursor:
        diccio[i[0]] = i[1]

    cursor.execute("SELECT ORIGEN, DISTANCIA FROM tren WHERE DESTINO = ?", (nodo,))
    for i in cursor:
        diccio[i[0]] = i[1]

    return diccio


# Devuelve la distancia en linea recta entre dos estaciones.
# Devuelve un entero.
def getDistanciaRecta(start, end):
    db = sqlite3.connect('metroDataBase.db')
    resultado = -1
    cursor = db.cursor()

    cursor.execute("SELECT DISTANCIA FROM recta WHERE ORIGEN = ? AND DESTINO = ?", (start, end))
    resultado = cursor.fetchall()

    if(resultado == []):
        cursor.execute("SELECT DISTANCIA FROM recta WHERE DESTINO = ? AND ORIGEN = ?", (start, end))
        resultado = cursor.fetchall()

    return resultado[0][0]


# Devuelve la linea a la que pertenece una estacion.
# Devuelve un entero.
#  EXPLIACION DE LAS LINEAS:
#    VERDE = 1
#    AMARILLA = 2
#    ROJA = 3
#    ROJA-VERDE-AMARILLA = 4
#    AMARILLA-VERDE = 5
#    AMARILLA-ROJA = 6
#    ROJA-VERDE = 7
def getLinea(nodo):
    db = sqlite3.connect('metroDataBase.db')
    cursor = db.cursor()

    cursor.execute("SELECT LINEA FROM ids WHERE ID = ?", (nodo,))
    resultado = cursor.fetchall()

    return resultado[0][0]
