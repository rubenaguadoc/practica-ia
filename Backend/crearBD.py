#!/usr/bin/python

import sqlite3 # Libreria de la BDD que vamos a usar.

def fillMetroTokyo(file, db):
    print("Insertando datos en la tabla: ", end="")

    data = file.readlines()
    i = 0

    for line in data:

        myLine = line.split()
        origen = myLine[0]
        destino = myLine[1]
        distancia = myLine[2]
        tiempo = myLine[3]

        db.execute("INSERT INTO metroTokyo (ID, ORIGEN, DESTINO, DISTANCIA, TIEMPO) VALUES (?, ?, ?, ?, ?)", (i, origen, destino, distancia, tiempo)); db.commit()

        i += 1

    print("EXITO \n");

def fillLineaVerde(file, db):
    print("Insertando datos en la tabla: ", end="")

    data = file.readlines()
    i = 0

    for line in data:

        myLine = line.split()
        origen = myLine[0]
        destino = myLine[1]
        distancia = myLine[2]

        db.execute("INSERT INTO lineaVerde (ID, ORIGEN, DESTINO, DISTANCIA) VALUES (?, ?, ?, ?)", (i, origen, destino, distancia)); db.commit()

        i += 1

    print("EXITO \n");

def fillRojaVerde(file, db):
    print("Insertando datos en la tabla: ", end="")

    data = file.readlines()
    i = 0

    for line in data:

        myLine = line.split()
        origen = myLine[0]
        destino = myLine[1]
        distancia = myLine[2]

        db.execute("INSERT INTO rojaVerde (ID, ORIGEN, DESTINO, DISTANCIA) VALUES (?, ?, ?, ?)", (i, origen, destino, distancia)); db.commit()

        i += 1

    print("EXITO \n");

# Crea una tabla exista o no. Si existe borra la que hay y crea una nueva.
def createTable(db):
    print("Creando la BDD del todo el Metro de Tokyo: ", end="") # end hace que el print de abajo se imprima seguido
    db.execute("DROP TABLE IF EXISTS metroTokyo")
    db.execute('''CREATE TABLE metroTokyo
                (
                ID        INT    PRIMARY KEY   NOT NULL,
                ORIGEN    TEXT                 NOT NULL,
                DESTINO   TEXT                 NOT NULL,
                DISTANCIA INT                  NOT NULL,
                TIEMPO    INT                  NOT NULL
                ); ''')
    print("EXITO \n")

    print("Creando la BDD de la linea Verde: ", end="") # end hace que el print de abajo se imprima seguido
    db.execute("DROP TABLE IF EXISTS lineaVerde")
    db.execute('''CREATE TABLE lineaVerde
                (
                ID        INT    PRIMARY KEY   NOT NULL,
                ORIGEN    TEXT                 NOT NULL,
                DESTINO   TEXT                 NOT NULL,
                DISTANCIA INT                  NOT NULL
                ); ''')
    print("EXITO \n")

    print("Creando la BDD de la linea Roja con la Verde: ", end="") # end hace que el print de abajo se imprima seguido
    db.execute("DROP TABLE IF EXISTS rojaVerde")
    db.execute('''CREATE TABLE rojaVerde
                (
                ID        INT    PRIMARY KEY   NOT NULL,
                ORIGEN    TEXT                 NOT NULL,
                DESTINO   TEXT                 NOT NULL,
                DISTANCIA INT                  NOT NULL
                ); ''')
    print("EXITO \n")

if __name__ == '__main__':
    print("")

    db = sqlite3.connect('metroDataBase.db')
    createTable(db)

    file = open("../MetroFiles/MetroTokyo.txt", 'r')
    fillMetroTokyo(file, db)
    file = open("../MetroFiles/LineaVerde.txt", 'r')
    fillLineaVerde(file, db)
    file = open("../MetroFiles/RojaVerde.txt", 'r')
    fillRojaVerde(file, db)

    db.close()
