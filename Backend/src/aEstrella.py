import metro

def algoritmo(inicio, fin):
    abiertos = [] # Lista de vecinos activos.
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
            if(i not in abiertos):
                abiertos.append(i) # Añadimos vecinos a abiertos
            else:
                vecinos[i] = -1

        for i in vecinos:
            if(i != -1):
                aux = acumulador + vecinos[i] + metro.getDistanciaRecta(cerrados[len(cerrados) - 1],fin)
                if(f > aux):
                    nodo = i
                    f = aux

        acumulador += vecinos[nodo]

        if(nodo == fin):
            cerrados.append(nodo)
            terminado = True
        else:
            if(nodo != inicio):
                cerrados.append(nodo)
                abiertos.remove(nodo)

    return cerrados



def main():
    path = algoritmo(1, 36) # Expected: [1, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 36]
    print(path)

main()
