#!/usr/bin/python

import sqlite3 # Libreria de la BDD que vamos a usar.

def fillMetroTokyo(file, db):
    print("Insertando distancias reales (el camino que hace el tren): ", end="")

    data = file.readlines()
    i = 0

    for line in data:

        myLine = line.split()
        origen = myLine[0]
        destino = myLine[1]
        distancia = myLine[2]
        tiempo = myLine[3]

        db.execute("INSERT INTO tren (ID, ORIGEN, DESTINO, DISTANCIA, TIEMPO) VALUES (?, ?, ?, ?, ?)", (i, origen, destino, distancia, tiempo)); db.commit()

        i += 1

    print("EXITO \n");

def fillLineaVerde(file, db):
    print("Insertando distancias en linea recta (osea, las que son 1001 conexiones): ", end="")

    data = file.readlines()
    i = 0

    for line in data:

        myLine = line.split()
        origen = myLine[0]
        destino = myLine[1]
        distancia = myLine[2]

        db.execute("INSERT INTO recta (ID, ORIGEN, DESTINO, DISTANCIA) VALUES (?, ?, ?, ?)", (i, origen, destino, distancia)); db.commit()

        i += 1

    print("EXITO \n");

def fillIds(file, db):
    print("Insertando datos de los ids: ", end="")

    data = file.readlines()
    i = 0

    for line in data:

        myLine = line.split()
        origen = myLine[0].upper()
        miId = myLine[1]

        db.execute("INSERT INTO ids (ORIGEN, ID) VALUES (?, ?)", (origen, miId)); db.commit()

        i += 1

    print("EXITO \n");


# Crea una tabla exista o no. Si existe borra la que hay y crea una nueva.
def createTable(db):
    print("Creando la BDD del todo el Metro de Tokyo: ", end="") # end hace que el print de abajo se imprima seguido
    db.execute("DROP TABLE IF EXISTS tren")
    db.execute('''CREATE TABLE tren
                (
                ID        INT    PRIMARY KEY   NOT NULL,
                ORIGEN    TEXT                 NOT NULL,
                DESTINO   TEXT                 NOT NULL,
                DISTANCIA INT                  NOT NULL,
                TIEMPO    INT                  NOT NULL
                ); ''')
    print("EXITO \n")

    print("Creando la BDD de la linea Verde: ", end="") # end hace que el print de abajo se imprima seguido
    db.execute("DROP TABLE IF EXISTS recta")
    db.execute('''CREATE TABLE recta
                (
                ID        INT    PRIMARY KEY   NOT NULL,
                ORIGEN    TEXT                 NOT NULL,
                DESTINO   TEXT                 NOT NULL,
                DISTANCIA INT                  NOT NULL
                ); ''')
    print("EXITO \n")

    print("Creando tabla ids: ", end="") # end hace que el print de abajo se imprima seguido
    db.execute("DROP TABLE IF EXISTS ids")
    db.execute('''CREATE TABLE ids
                (
                ID        INT    PRIMARY KEY   NOT NULL,
                ORIGEN    TEXT                 NOT NULL
                ); ''')
    print("EXITO \n")

if __name__ == '__main__':
    print("")

    db = sqlite3.connect('metroDataBase.db')
    createTable(db)

    file = open("../MetroFiles/tren.txt", 'r')
    fillMetroTokyo(file, db)
    file = open("../MetroFiles/recta.txt", 'r')
    fillLineaVerde(file, db)
    file = open("../MetroFiles/ids.txt", 'r')
    fillIds(file, db)

    db.close()
