import metro


def decodeLineNumber(num):
    if(num == 4):
        return [1, 2, 3]
    elif(num == 5):
        return [1, 2]
    elif(num == 6):
        return [2, 3]
    elif(num == 7):
        return [1, 3]
    else:
        return [num]


def lineasMetro(lista):

    colores = []

    for i in range(0, len(lista)):
        miColor = decodeLineNumber(metro.getLinea(lista[i]))
        if(len(miColor) > 1):
            # Miro a la siguiente estación si existe.
            if(i+1 < len(lista)):
                siguienteColor = decodeLineNumber(metro.getLinea(lista[i+1]))
                coloresGanadores = list(
                    filter(lambda x: x in siguienteColor, miColor))

                # Si hay mas de un color ganador, miro mi anterior (si lo hay)
                if(i-1 >= 0 and len(coloresGanadores) > 1):
                    anteriorColor = decodeLineNumber(metro.getLinea(lista[i-1]))
                    coloresEmergencia = list(filter(lambda x: x in anteriorColor, coloresGanadores))

                    # Si ni con esas salimos de dudas, vemos el siguiente del siguiente
                    if(len(coloresEmergencia) > 1):
                        if(i+2 < len(lista)):
                            superSiguienteColor = decodeLineNumber(metro.getLinea(lista[i+2]))
                            coloresSuperMalvados = list(
                                filter(lambda x: x in superSiguienteColor, coloresEmergencia))
                            # AÑADO COLOR
                            colores.append(coloresSuperMalvados[0])

                        else:
                            colores.append(coloresEmergencia[0]) # AÑADO COLOR

                    elif(len(coloresEmergencia) == 1):  # Si nos basta con el anterior me meto aquí
                        colores.append(coloresEmergencia[0]) # AÑADO COLOR
                    else:
                        colores.append(coloresGanadores[0]) # AÑADO COLOR

                elif(len(coloresGanadores) > 1):  # Si nos basta con el siguiente me meto aquí
                    if(i+2 < len(lista)):
                        superSiguienteColor = decodeLineNumber(metro.getLinea(lista[i+2]))
                        coloresSuperMalvados = list(filter(lambda x: x in superSiguienteColor, coloresGanadores))
                        if(len(coloresSuperMalvados) >= 1):
                            colores.append(coloresSuperMalvados[0]) # AÑADO COLOR
                        else:
                            colores.append(coloresGanadores[0]) # AÑADO COLOR
                    elif(len(coloresGanadores) == 1):
                        colores.append(coloresGanadores[0]) # AÑADO COLOR
                else:
                    if(i-1 >= 0):
                        if(lista[i-1] == 36 and lista[i] == 5):
                            colores[len(colores)-1] = 3
                            colores.append(3)
                        else:
                            colores.append(coloresGanadores[0]) # AÑADO COLOR
                    else:
                        colores.append(coloresGanadores[0]) # AÑADO COLOR
            else:  # si soy la última estación, comparo con el anterior
                anteriorColor = decodeLineNumber(metro.getLinea(lista[i-1]))
                ganador = list(filter(lambda x: x in anteriorColor, miColor))
                # Miro la anterior de la anterior.
                if(len(ganador) > 1 and i-2 >= 0):
                    anteriorAnteriorColor = decodeLineNumber(metro.getLinea(lista[i-1]))
                    oldColor = list(filter(lambda x: x in anteriorAnteriorColor, ganador))
                    colores.append(oldColor[0]) # AÑADO COLOR

                else:  # me basta con el anterior
                    colores.append(ganador[0]) # AÑADO COLOR

        else:  # Solo hay un color, menos mal :)
            colores.append(miColor[0]) # AÑADO COLOR

    return colores


def algoritmo(inicio, fin, transbordo):
    initialDistance = metro.getDistanciaRecta(inicio, fin) if inicio != fin else 0
    listaAbierta = {inicio: {"g": 0, "h": initialDistance, "f": initialDistance, "padre": -1}}
    listaCerrada = {}  # {idNodo: idNodoPadre}
    finalWeight = 0

    # f(n) = g(n) + h(n)
    while(fin not in listaCerrada.keys()):
        thisNodeId = sorted(listaAbierta, key=lambda elem: listaAbierta[elem]["f"])[0]
        thisNode = listaAbierta[thisNodeId].copy()
        thisNodeLines = set(decodeLineNumber(metro.getLinea(thisNodeId)))

        if(thisNodeId == fin):
            finalWeight = thisNode["f"]
        
        listaCerrada[thisNodeId] = thisNode["padre"]
        del listaAbierta[thisNodeId]

        vecinos = metro.getDistanciaTren(thisNodeId)  # [{idVecino: distanciaAel}, ...]

        vecinos = dict(filter(lambda vecino: vecino[0] not in listaCerrada, vecinos.items()))
        if(len(vecinos) == 0):
            continue

        for idVecino, distanciVecino in vecinos.items():
            vecinoLines = set(decodeLineNumber(metro.getLinea(idVecino)))
            prevNodeLines = set(decodeLineNumber(metro.getLinea(thisNode["padre"]))) if thisNode["padre"] != -1 else set([1, 2, 3])
            specialCase = thisNode["padre"] in [5, 20] and idVecino in [5, 20]  # Caso especial no detectable de otra manera cuando se va por la linea roja

            g = thisNode["g"] + distanciVecino + 300  # Cuantas menos paradas, mejor, cada parada añade un delay de 1/3 de trayecto entre estaciones

            if(len(thisNodeLines & vecinoLines & prevNodeLines) == 0 or specialCase):
                g += 1250 if not transbordo else 1000000  # Penalización equibalente a 1 parada y cuarto

            h = 0 if idVecino == fin else metro.getDistanciaRecta(idVecino, fin)
            f = g + h

            if(idVecino not in listaAbierta or listaAbierta[idVecino]["f"] > f):
                listaAbierta[idVecino] = {"g": g, "h": h, "f": f, "padre": thisNodeId}

    pathList = []
    while(fin != -1):
        pathList.append(fin)
        fin = listaCerrada[fin]

    result = list(reversed(pathList))
    return result, lineasMetro(result), finalWeight

def main():
    res, color, basura = algoritmo(19, 4, False)
    for i in range(0, len(res)):
        print(res[i], "::", color[i])

main()
