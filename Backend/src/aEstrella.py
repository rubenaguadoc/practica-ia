import metro

def algoritmo(inicio, fin):
    abiertos = []
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
            if(i not in abiertos and i not in cerrados):
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

    return cerrados



def main():
    path = algoritmo(1, 36) # Ikebukuro -> Ochanomizu
    print("Solucion ::", path, end=" ")
    print(path == [1, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 36])

    path = algoritmo(7, 20) # Harajuko -> Akihabara
    print("Solucion ::", path, end=" ")
    print(path == [7, 6, 30, 31, 32, 33, 34, 35, 36, 20])

    path = algoritmo(32, 18)
    print("Solucion ::", path, end=" ")
    print(path == [32, 33, 34, 35, 36, 18])

main()
