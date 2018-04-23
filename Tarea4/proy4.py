from math import sqrt, ceil, sin, cos, pi, floor
from random import randint, uniform, random
import time, random

class Grafo:
    def __init__(self):
        self.dis=dict()
        self.vecinos=dict()
        self.aristas=[]
        self.nodos=[]
        self.A=[]
        self.V= dict()
        self.E=dict()
        
    #nodos al rededor del centro
    def agrega(self, v, c, rad, ang):
        with open("Nodos.dat", "w") as crear:
            for n in range(1, v+1):
                x = rad*cos(ang*n) + c[0]
                y = rad*sin(ang*n) + c[1]
                self.V[v]=(x,y)
                self.nodos.append((x,y))
                print(x, y, file = crear)
                if not (x, y) in self.vecinos:
                    self.vecinos[(x,y)] = []

    #conectaremos nodos correspondientes en k
    def conecta(self, k):
        for j in range(0,v):
            x1 = self.nodos[j][0]
            y1 = self.nodos[j][1]
            for r in range(1,k+1):
                x2 = self.nodos[j-r][0]
                y2 = self.nodos[j-r][1]
                #conexión
                #self.E[(a, b)] = self.E[(b, a)]=r
                self.aristas.append((x1,y1,x2,y2))
                #self.aristas[(a,b)] = self.aristas[(b,a)] = r
                #self.vecinos[a].append(b)
                #self.vecinos[b].append(a)

    def Inter(self, h, m, v):
        prob=random()
        maxi=0.2
        if prob > maxi:
            for g in range(v):
                t1=self.nodos[h][0]
                n1=self.nodos[h][1]
                t2=self.nodos[m][0]
                n2=self.nodos[m][1]
                self.aristas.append((t1,n1,t2,n2))

    def intermedio(self, h, m):
        prob=random()
        maxi=0.2
        if prob > maxi:
            p=self.nodos[h]
            q=self.nodos[m]
            self.aristas[(p,q)]=self.aristas[(q,p)]=h
            self.vecinos[p].append(q)
            self.vecinos[q].append(p)

    def floyd_warshall(self):
        self.d = {}
        for (x,y) in self.nodos:
            self.d[((x,y),(x,y))] = 0 # distancia reflexiva es cero
            for u in self.vecinos[(x,y)]: # para vecinos, la distancia es el peso
                self.d[((x,y),u)] = self.aristas[((x,y),u)]
        for intermedio in self.nodos:
            for desde in self.nodos:
                for hasta in self.nodos:
                    di = None
                    if (desde, intermedio) in self.d:
                        di = self.d[(desde, intermedio)]
                    ih = None
                    if (intermedio, hasta) in self.d:
                        ih = self.d[(intermedio, hasta)]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (desde, hasta) not in self.d or c < self.d[(desde, hasta)]:
                            self.d[(desde, hasta)] = c # mejora al camino actual
        return self.d
    
        def Coeficiente(self):
        self.sumDis = 0
        for u in self.d:
            self.sumDis = self.sumDis + self.d[u]
        self.argDis = self.sumDis/len(self.d)
        self.densidad = []
        for (x,y) in self.nodos:
            self.lpq = []
            for lpq2 in self.aristas:
                self.lpq.append(lpq2)
            numvecino = len(self.vecinos[(x,y)]) -1
            for t in range(numvecino):
                print("el vecino es")
                
                self.clustCoef = 0
                h = self.vecinos[(x,y)][t]
                print(h)
                for m in self.vecinos[h]:
                    
                    if m in self.vecinos[(x,y)] and m is not (x,y) and m is not (y,x):
                        print("el vecino del vecino es")
                        print(m)
                        if (h,m) in self.lpq:
                            self.lpq.remove((h,m))
                            self.clustCoef = self.clustCoef + 1
                       
            dens = 2*self.clustCoef/((numvecino)*(numvecino-1))
            self.densidad.append(dens)
            
    def grafos(self ,h ,m ,v):
        with open("tareaT4.plot","w") as archivo:
            print("set term png", file=archivo)
            print("set output 'tarea4.png'", file=archivo)
            print("set xrange [-0.1:1.1]", file=archivo)
            print("set yrange [-0.1:1.1]", file=archivo)
            print("set pointsize 1", file=archivo)
            print("set size square", file=archivo)
            print("set key off", file=archivo)
            num=0
            for a in self.aristas:

                (x1,y1,x2,y2)=a

                (t1,n1,t2,n2)=a
                print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead filled lw 1".format(num+1,x1,y1,x2,y2),file=archivo)
                print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead filled lw 1".format(num+1,t1,n1,t2,n2),file=archivo)
                num+=1
            print("show arrow", file=archivo)
            print("plot 'Nodos.dat' using 1:2 with points pt 7", file=archivo)
            print("quit()", file=archivo)

v=15
mu=(v+1)//2
k=2
if k>mu:
    k=k-1
else:
    k=k

h=uniform(0,v)
m=uniform(0,v)
if h==m and h==(m-k) and h==(m+k):
    m=uniform(0,v)
else:
    m=m
c = (0.5, 0.5)
rad = 0.4
ang = (360/v)*(pi/180)
G=Grafo()
G.agrega(v, c, rad, ang)
G.conecta(k)
G.Inter
G.floy_warshall
G.Coeficiente
G.grafos(h,m,v)



