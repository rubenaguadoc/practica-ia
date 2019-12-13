import sys
import traceback
import aEstrella


def test():
    for i in range(1, 37):
        print(i)
        for j in range(1, 37):
            try:
                aEstrella.algoritmo(i, j, True)
                aEstrella.algoritmo(i, j, False)
            except Exception:
                _, _, exc_traceback = sys.exc_info()
                stack = traceback.extract_tb(exc_traceback, limit=2)[1]
                print("El trayecto ", i, j, "ha fallado en la linea", stack.lineno, "-->", stack.line)


test()
