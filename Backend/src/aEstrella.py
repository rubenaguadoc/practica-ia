import metro

def hazMagia(num):
    if(num == 4):
        return {1, 2, 3}
    if(num == 5):
        return {2, 1}
    if(num == 6):
        return {2, 3}
    if(num == 7):
        return {1, 3}
    else:
        return {num}

def algoritmo(inicio, fin, trasbordo):
    if(inicio == fin):
        return [inicio]

    abiertos = []
    cerrados = []
    cerrados.append(inicio)

    if(trasbordo): # Trasbordo TRUE = Hay que evitar trasbordos
        lineaDios = hazMagia(metro.getLinea(inicio)) & hazMagia(metro.getLinea(fin))
        if(len(lineaDios) == 0):
            print("ERROR :: Camino no existente.")
            return 0, 0

    terminado = False
    acumulador = 0

    # Movida de las interseccions:
    aux = {1, 2, 3}
    siguiente = {}
    anterior = {}
    actual = {}
    tuplita = 0
    colores = []


    # f(n) = g(n) + h(n)
    while(not terminado):
        tuplita = hazMagia(metro.getLinea(cerrados[len(cerrados) - 1]))
        if(len(tuplita) == 1):
            anterior = actual
            actual = tuplita
        else:
            aux = tuplita
            anterior = actual
            actual = aux & tuplita

        vecinos = metro.getDistanciaTren(cerrados[len(cerrados) - 1]) # Vecinos del nodo
        f = 1000000 # variable muy grande para luego quedarnos con la f() mas peque
        nodo = 0 # nodo siguiente al que nos movemos

        for i in vecinos:
            if(trasbordo and i not in cerrados and len(hazMagia(metro.getLinea(i)) & lineaDios) != 0):
                abiertos.append(i) # Añadimos vecinos a abiertos
            elif(not trasbordo and i not in cerrados):
                abiertos.append(i) # Añadimos vecinos a abiertos
            elif(trasbordo and i not in cerrados and len(hazMagia(metro.getLinea(i)) & lineaDios) == 0):
                return 0, 0
            else:
                vecinos[i] = -1
        

        print(vecinos)
        for i in vecinos:
            if(vecinos[i] != -1 and i != fin):
                auxilio = acumulador + vecinos[i] + metro.getDistanciaRecta(i,fin)
                if(f > auxilio):
                    nodo = i
                    f = auxilio
            elif(i == fin):
                nodo = i
                break


        acumulador += vecinos[nodo]

        if(nodo == fin):
            if(len(actual) > 1):
                siguiente = hazMagia(metro.getLinea(nodo))
                aux = actual & siguiente
                colores.append(aux)
            else:
                colores.append(actual)
            colores.append(colores[len(colores) - 1])
            cerrados.append(nodo)
            terminado = True
        else:
            if(len(actual) > 1):
                siguiente = hazMagia(metro.getLinea(nodo))
                aux = actual & siguiente
                colores.append(aux)
            else:
                colores.append(actual)
            if(nodo != inicio):
                cerrados.append(nodo)
                abiertos.remove(nodo)

    cont = 0
    for i in colores:
        if (len(i) > 1):
            colores[cont] = colores[cont + 1]
        cont += 1

    return cerrados, colores

def main():
    res = algoritmo(2, 36, False)
    for i in res: print(i, " ", end="")
    print()
    
   # res = algoritmo(2, 36, True)
   # for i in res: print(i, " ", end="")
   # print()
   # print()
   # print()
   # res = algoritmo(14, 34, False)
   # for i in res: print(i, " ", end="")
   # print()
   # 
   # res = algoritmo(14, 34, True)
   # for i in res: print(i, " ", end="")
   # print()
   # 
   # res = algoritmo(6, 22, False)
   # for i in res: print(i, " ", end="")
   # print()
   # 
   # res = algoritmo(6, 22, True)
   # for i in res: print(i, " ", end="")
   # print()

main()
