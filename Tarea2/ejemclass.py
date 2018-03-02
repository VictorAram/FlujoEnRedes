from random import uniform
from math import ceil, sqrt

def distancia(p,q):
    return sqrt(((p[0]-q[0])**2)+((p[1]-q[1])**2))

class Grafo:
    def __init__(tablon, orden=10):
        tablon.n = orden
        tablon.m = ceil(orden/5)
        tablon.nodos = []
        tablon.aristas = []
        tablon.Eu = []

    def CreaNodos(tablon):
        for t in range(tablon.n):
            aux=1
            p=5
            x=uniform(1,30)
            y=uniform(1,30)
            tablon.nodos.append((x,y))
            print(x,y,file=crear)
            
    def CreaAristas(tablon):
        with open ("nodos.dat", "w") as crear:
            t=0
            f=0
            for t in range(tablon.n):
                Eu.append([])
                for f in range(tablon.n):
                    Eu[t].append(None)
            t=0
            f=0
            for t in range(tablon.n):
                x1=nodos[t][0]
                y1=nodos[t][1]
                for f in range(tablon.n):
                    g1=nodos[f][0]
                    g2=nodos[f][1]
                    Eu[t][f]=math.sqrt(((g2-y1)**2)+((g1-x1)**2))
                    if Eu[t][f]<10:
                        aristas.append((x1,y1,g1,g2))

G=Grafo()
G.CreaNodos()
G.CreaAristas()

with open("tarea2.plot","w") as archivo:
    print("set term pdf", file=archivo)
    print("set output 'graficat2.pdf", file=archivo)
    print("set xrange [0:30]", file=archivo)
    print("set yrange [0:30]", file=archivo)
    print("set pointsize 3", file=archivo)
    print("set size square", file=archivo)
    print("set key off", file=archivo)
    num=1

    for a in G.aristas:
        (x1,y1,x2,y2)=a
        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled lw 1".format(num,x1,y1,x2,y2),file=archivo)
        num+=1

    print("show arrow", file=archivo)
    print("plot 'nodos.dat' using 1:2 with points pt 7", file=archivo)
    print("quit()",file=archivo) 
