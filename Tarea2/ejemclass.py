from random import uniform
from math import sqrt

class Grafo:
    def __init__(tablon):
        tablon.n=15
        tablon.nodos = []
        tablon.aristas = []
        tablon.Eu= []

    def Nodos (tablon):
        with open ("nodos.dat", "w") as crear:
            for t in range(tablon.n):
                x=uniform(1,30)
                y=uniform(1,30)
                tablon.nodos.append((x,y))
                print(x,y, file=crear)

    
    def Aris (tablon):
        for j in range(tablon.n):
            x1= tablon.nodos[j][0]
            y1= tablon.nodos[j][1]
            for f in range(tablon.n):
                g1=tablon.nodos[f][0]
                g2=tablon.nodos[f][1]
                tablon.Eu=sqrt(((g2-y1)**2)+((g1-x1)**2))
                if tablon.Eu<10:
                    tablon.aristas.append((x1,y1,g1,g2))

    def graficar(self, di):
        with open("hoy.plot","w") as archivo:
             print("set term pdf", file=archivo)
             print("set output 'hoy.pdf'", file=archivo)
             print("set xrange [0:30]", file=archivo)
             print("set yrange [0:30]", file=archivo)
             print("set pointsize .7", file=archivo)
             print("set size square", file=archivo)
             print("set key off", file=archivo)
             num=0
             for a in self.aristas:
                 (x1,y1,g1,g2)=a
                 if di is 1:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled lw 1".format(num+1,x1,y1,g1,g2),file=archivo)
                 else:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead filled lw 1".format(num+1,x1,y1,g1,g2),file=archivo)
                 num+=1
             print("show arrow", file=archivo)
             print("plot 'nodos.dat' using 1:2 with points pt 7 lc 6", file=archivo)
             print("quit()",file=archivo)

G = Grafo()
G.Nodos()
G.Aris()
G.graficar(di=1) 
