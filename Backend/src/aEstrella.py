import metro

def decoder(num):
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
        miColor = decoder(metro.getLinea(lista[i]))
        if(len(miColor) > 1):
            # Miro a la siguiente estación si existe.
            if(i+1 < len(lista)):
                siguienteColor = decoder(metro.getLinea(lista[i+1]))
                coloresGanadores = list(filter(lambda x  : x in siguienteColor, miColor))

                # Si hay mas de un color ganador, miro mi anterior (si lo hay)
                if(i-1 >= 0 and len(coloresGanadores) > 1):
                    anteriorColor = decoder(metro.getLinea(lista[i-1]))
                    coloresEmergencia = list(filter(lambda x  : x in anteriorColor, coloresGanadores))
                    
                    # Si ni con esas salimos de dudas, vemos el siguiente del siguiente
                    if(len(coloresEmergencia) > 1):
                        if(i+2 < len(lista)):
                            superSiguienteColor = decoder(metro.getLinea(lista[i+2]))
                            coloresSuperMalvados = list(filter(lambda x  : x in superSiguienteColor, coloresEmergencia))
                            
                            # Y ya si con esas no va, se añade el primero de los numeros por que si.
                            if(len(coloresSuperMalvados) > 1):
                                colores.append(coloresGanadores[0]) # AÑADO COLOR
                            else: # Si el siguiente del siguiente va bien al fin
                                colores.append(coloresSuperMalvados[0])
                        else:
                            colores.append(coloresEmergencia[0])

                    else: # Si nos basta con el anterior me meto aquí
                        colores.append(coloresEmergencia[0])

                else: # Si nos basta con el siguiente me meto aquí
                    colores.append(coloresGanadores[0])
            else: # si soy la última estación, comparo con el anterior
                anteriorColor = decoder(metro.getLinea(lista[i-1]))
                ganador = list(filter(lambda x  : x in anteriorColor, miColor))
                if(len(ganador) > 1 and i-2 >= 0): # Miro la anterior de la anterior.
                    anteriorAnteriorColor = decoder(metro.getLinea(lista[i-1]))
                    oldColor = list(filter(lambda x  : x in anteriorAnteriorColor, ganador))

                    if(len(oldColor) > 1): # me pego un tiro y añado lo que quiera
                        colores.append(ganador[0])
                    else:
                        colores.append(oldColor[0])
                else: # me basta con el anterior
                    colores.append(ganador[0])

        else: # Solo hay un color, menos mal :)
            colores.append(miColor[0])

    return colores

def algoritmo(inicio, fin, trasbordo):
    if(inicio == fin):
        return [inicio]

    cerrados = []
    cerrados.append(inicio)

    terminado = False
    acumulador = 0

    # f(n) = g(n) + h(n)
    while(not terminado):

        vecinos = metro.getDistanciaTren(cerrados[len(cerrados) - 1]) # Vecinos del nodo
        f = 1000000 # variable muy grande para luego quedarnos con la f() mas peque
        nodo = 0 # nodo siguiente al que nos movemos

        for i in vecinos:
            if(i in cerrados):
                vecinos[i] = -1
        

        for i in vecinos:
            if(vecinos[i] != -1 and i != fin):
                suma = 0
                if(trasbordo and metro.getLinea(i) > 3):
                    suma = 100000
                aux = acumulador + vecinos[i] + suma + metro.getDistanciaRecta(i,fin)
                if(f > aux):
                    nodo = i
                    f = aux

            elif(i == fin):
                nodo = i
                break

        acumulador += vecinos[nodo]

        if(nodo == fin):
            cerrados.append(nodo)
            terminado = True
        else:
            if(nodo != inicio):
                cerrados.append(nodo)

    colores = lineasMetro(cerrados)
    return cerrados, colores

def main():
    linea, color = algoritmo(30, 22, False)
    for i in linea:
        print(i, end = " ")
    print()
    for j in color:
        print(j, end = " ")
    print()
    print(len(linea))
    print(len(color))

main()
