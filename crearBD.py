#!/usr/bin/python

import sqlite3 # Libreria de la BDD que vamos a usar.
import argparse # Libreria para pasar argumentos al llamar al script
import ezodf # Libreria para leer del excel

# Crea una tabla exista o no. Si existe borra la que hay y crea una nueva.
def createTable(excel, db):
    if(excel == "MetroTokyo.ods"):
        print("Creando la BDD del Metro de Tokyo: ", end="") # end hace que el print de abajo se imprima seguido
        db.execute("DROP TABLE IF EXISTS metroTokyo")
        db.execute('''CREATE TABLE metroTokyo
                    (
                    ID        INT    PRIMARY KEY   NOT NULL,
                    ORIGEN    TEXT                 NOT NULL,
                    DESTINO   TEXT                 NOT NULL,
                    DISTANCIA INT                  NOT NULL,
                    TIEMPO    INT                  NOT NULL
                    ); ''')
        print("EXITO \n \n")

    if(excel == "LineaVerde.ods"):
        print("Creando la BDD de la Linea Verde: ", end="") # end hace que el print de abajo se imprima seguido
        db.execute("DROP TABLE IF EXISTS metroTokyo")
        db.execute('''CREATE TABLE metroTokyo
                    (
                    ID        INT    PRIMARY KEY   NOT NULL,
                    ORIGEN    TEXT                 NOT NULL,
                    DESTINO   TEXT                 NOT NULL,
                    DISTANCIA INT                  NOT NULL,
                    ); ''')
        print("EXITO \n \n")



def fillTable(excel, db):
    print("Insertando datos en la tabla: ", end="")
    db.execute('''INSERT INTO metroTokyo
               (ID, ORIGEN, DESTINO, DISTANCIA, TIEMPO) VALUES
               (1, "micasa", "tucasa", 1000, 1923)
               ''');
    db.commit()
    print("EXITO")

def showTable(excel, db):
    cursor = db.execute("SELECT ID, origen, destino, distancia, tiempo FROM metroTokyo");
    for row in cursor:
        print("ID = ", row[0])
        print("origen = ", row[1])
        print("destino = ", row[2])
        print("distancia = ", row[3])
        print("tiempo = ", row[4], "\n")

def callMe(doc):
    print("Spreadsheet contains %d sheet(s)." % len(doc.sheets))
    for sheet in doc.sheets:
        print("-"*40)
        print("   Sheet name : '%s'" % sheet.name)
        print("Size of Sheet : (rows=%d, cols=%d)" % (sheet.nrows(), sheet.ncols()) )


if __name__ == '__main__':

    # Selecciona de que excel se quiere hacer la BDD
    parser = argparse.ArgumentParser()
    parser.add_argument('--table', help="Selecciona la tabla que quieres crear.")
    args = parser.parse_args()

    # Esto es para mantener la estructura del excel.
    ezodf.config.set_table_expand_strategy('all')
    ods = ezodf.opendoc(args.table)

    callMe(ods)

    # args.table = "MetroFiles/MetroTokyo.ods" y pasa a ser "MetroTokyo.ods" por ejemplo.
    args = args.table[11:]

    db = sqlite3.connect('metroDataBase.db')

    createTable(args, db)
    fillTable(args, db)
    showTable(args, db)

    db.close()
    ezodf.config.reset_table_expand_strategy()
