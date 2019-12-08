import metro

def algoritmo(inicio, fin, trasbordo):
    if(inicio == fin):
        return [inicio]

    abiertos = []
    cerrados = []
    cerrados.append(inicio)

    if(trasbordo): # Trasbordo TRUE = Hay que evitar trasbordos
        lineaDios = metro.getLinea(inicio)

    terminado = False
    acumulador = 0

    # f(n) = g(n) + h(n)
    while(not terminado):
        vecinos = metro.getDistanciaTren(cerrados[len(cerrados) - 1]) # Vecinos del nodo
        f = 1000000 # variable muy grande para luego quedarnos con la f() mas peque
        nodo = 0 # nodo siguiente al que nos movemos

        for i in vecinos:
            if(trasbordo and i not in cerrados and metro.getLinea(i) == lineaDios):
                abiertos.append(i) # Añadimos vecinos a abiertos
            elif(not trasbordo and i not in cerrados):
                abiertos.append(i) # Añadimos vecinos a abiertos
            else:
                vecinos[i] = -1

        for i in vecinos:
            if(vecinos[i] != -1 and i != fin):
                aux = acumulador + vecinos[i] + metro.getDistanciaRecta(i,fin)
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
                abiertos.remove(nodo)

    linea = []
    for i in cerrados:
        linea.append(metro.getLinea(i))

    return cerrados, linea
