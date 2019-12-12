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

    linea = []
    for i in cerrados:
        linea.append(metro.getLinea(i))

    return cerrados, linea

def main():
    res = algoritmo(1, 36, False)
    for i in res:
        print(i, end = " ")

main()
