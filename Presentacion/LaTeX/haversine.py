from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):

    coord = open("../../coordenadas.txt", 'r')
    respueta = open("../../recta.txt", 'w')
    data = coord.readLines()

    listaDeDatos = []

    for line in data:
        myLine = line.split()

        lon1 = myLine[0]
        lat1 = myLine[1]
        lon2 = myLine[2]
        lat2 = myLine[3]

        # convertimos grados en radianes
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371000 # Radio de la tierra en metros

        listaDeDatos.append(c*r)

    for i in listaDeDatos:
        respuesta.write(i)

