#!/usr/bin/python

import sqlite3 # Libreria de la BDD que vamos a usar.
import os

def fillMetroTokyo(file, db):
    print("Insertando distancias reales (el camino que hace el tren): ", end="")

    data = file.readlines()
    cursor = db.cursor()

    for line in data:
        myLine = line.split()
        cursor.execute("SELECT ID FROM ids WHERE NOMBRE='" + myLine[0] + "'");
        for i in cursor:
            origen = i[0]
            break # por si aca que no se como va esto :3
        cursor.execute("SELECT ID FROM ids WHERE NOMBRE='" + myLine[1] + "'");
        for i in cursor:
            destino = i[0]
            break # por si aca que no se como va esto :3

        distancia = myLine[2]
        tiempo = myLine[3]

        db.execute("INSERT INTO tren (ORIGEN, DESTINO, DISTANCIA, TIEMPO) VALUES (?, ?, ?, ?)", (origen, destino, distancia, tiempo)); db.commit()

    print("EXITO \n");

def fillLineaVerde(file, db):
    print("Insertando distancias en linea recta (osea, las que son 1001 conexiones): ", end="")

    data = file.readlines()
    cursor = db.cursor()

    for line in data:

        myLine = line.split()
        cursor.execute("SELECT ID FROM ids WHERE NOMBRE='" + myLine[0] + "'");
        for i in cursor:
            origen = i[0]
            break # por si aca que no se como va esto :3
        cursor.execute("SELECT ID FROM ids WHERE NOMBRE='" + myLine[1] + "'");
        for i in cursor:
            destino = i[0]
            break # por si aca que no se como va esto :3
        distancia = myLine[2]

        db.execute("INSERT INTO recta (ORIGEN, DESTINO, DISTANCIA) VALUES (?, ?, ?)", (origen, destino, distancia)); db.commit()

    print("EXITO \n");

def fillIds(file, db):
    print("Insertando datos de los ids: ", end="")

    data = file.readlines()
    i = 0

    for line in data:

        myLine = line.split()
        miId = myLine[0]
        nombre = myLine[1].upper()
        linea = myLine[2]

        db.execute("INSERT INTO ids (ID, NOMBRE, LINEA) VALUES (?, ?, ?)", (miId, nombre, linea)); db.commit()

        i += 1

    print("EXITO \n");


# Crea una tabla exista o no. Si existe borra la que hay y crea una nueva.
def createTable(db):
    print("Creando la tabla de los datos de los trenes: ", end="") # end hace que el print de abajo se imprima seguido
    db.execute("DROP TABLE IF EXISTS tren")
    db.execute('''CREATE TABLE tren
                (
                ORIGEN    INT                  NOT NULL,
                DESTINO   INT                  NOT NULL,
                DISTANCIA INT                  NOT NULL,
                TIEMPO    INT                  NOT NULL
                ); ''')
    print("EXITO \n")

    print("Creando la tabla de los datos de las lineas rectas: ", end="") # end hace que el print de abajo se imprima seguido
    db.execute("DROP TABLE IF EXISTS recta")
    db.execute('''CREATE TABLE recta
                (
                ORIGEN    INT                  NOT NULL,
                DESTINO   INT                  NOT NULL,
                DISTANCIA INT                  NOT NULL
                ); ''')
    print("EXITO \n")

    print("Creando tabla ids: ", end="") # end hace que el print de abajo se imprima seguido
    db.execute("DROP TABLE IF EXISTS ids")
    db.execute('''CREATE TABLE ids
                (
                ID        INT    PRIMARY KEY   NOT NULL,
                NOMBRE    TEXT                 NOT NULL,
                LINEA     INT                  NOT NULL
                ); ''')
    print("EXITO \n")

if __name__ == '__main__':
    print("")

    try:
        os.remove("./metroDataBase.db")
    except Exception:
        pass
    db = sqlite3.connect('metroDataBase.db')
    createTable(db)

    file = open("../MetroFiles/ids.txt", 'r')
    fillIds(file, db)
    file = open("../MetroFiles/tren.txt", 'r')
    fillMetroTokyo(file, db)
    file = open("../MetroFiles/recta.txt", 'r')
    fillLineaVerde(file, db)

    db.close()
