import metro

def magia(num):
    if(num == 4):
        return {1, 2, 3} 
    elif(num == 5):
        return {1, 2}
    elif(num == 6):
        return {2, 3}
    elif(num == 7):
        return {1, 3}
    else:
        return {num}

def aplicarColores(inicio, fin, trasbordo):
    cerrados, colores = algoritmo(inicio, fin, trasbordo)

    anterior = 0
    siguiente = 0
    actual = 0

    aAnterior = 0
    sSiguiente = 0

    auxxx = 0
    
    lineas = []
    for elem in colores:
        contador = 0
        for i in elem:
            if(contador == 0):
                anterior = i
            elif(contador == 1):
                actual = i
            else:
                siguiente = i
            contador += 1

        if(len(actual) == 1):
            if(aAnterior != 0):
                for i in actual:
                    lineas.append(i)
                    lineas.append(i)
            else:
                for i in actual:
                    lineas.append(i)
        else:
            if(aAnterior == 0):
                aAnterior = actual
            else:
                actual = aAnterior & actual
                if(len(actual) > 1):
                    auxxx = {lineas.append(lineas[len(lineas) - 1]) and actual}
                    if(len(auxxx) != 0):
                        miniContador = 0
                        for i in actual:
                            if(miniContador == 1):
                                lineas.append(i)
                            miniContador += 1
                    else:
                        for i in auxxx:
                            lineas.append(i)

                    aAnterior = 0
                else:
                    for i in actual:
                        lineas.append(i)
                    aAnterior = 0

    if(len(colores) != len(lineas)):
        lineas.append(lineas[len(lineas)])

    return cerrados, lineas

def algoritmo(inicio, fin, trasbordo):
    if(inicio == fin):
        return [inicio]

    cerrados = []
    cerrados.append(inicio)

    terminado = False
    acumulador = 0
    flag = False

    colores = []
    anterior = 0
    actual = 0
    siguiente = 0

    # f(n) = g(n) + h(n)
    while(not terminado):


        anterior = actual
        actual = magia(metro.getLinea(cerrados[len(cerrados) - 1]))


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

        siguiente = magia(metro.getLinea(nodo))
        colores.append((anterior, actual, siguiente))

        if(not flag):

            if(nodo == fin):
                cerrados.append(nodo)
                flag = True
            else:
                if(nodo != inicio):
                    cerrados.append(nodo)
        else:
            terminado = True

    return cerrados, colores

def main():
#    res = aplicarColores(2, 36, False)
#    for i in res:
#        print(i, end = " ")
#
#
#    print()
#    res = aplicarColores(1, 20, False)
#    for i in res:
#        print(i, end = " ")
#
#
#    print()
#    res = aplicarColores(17, 35, False)
#    for i in res:
#        print(i, end = " ")


    print()
    res = aplicarColores(21, 6, True)
    for i in res:
        print(i, end = " ")


main()
