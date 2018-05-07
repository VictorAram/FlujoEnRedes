from random import uniform
from random import random
from math import sqrt

class Grafo:
    def __init__(self):
        self.nodos=[]
        self.aristas=[]
        self.nodos2=[]
        self.aristas2=[]

    def Nodos (self, n):
        with open("nodos.dat","w") as crear:
            x=2
            for t in range(n):
                x=x+1
                y=1
                for g in range(n):
                    y=y+1
                    self.nodos.append((x,y))
                    print(x,y, file=crear)

    def Aris(self,n,l):
        prob=0.999
        if l==0:
            print("no hay conexiones")
        for i in range((n*n)):
            x1=self.nodos[i][0]
            y1=self.nodos[i][1]
            for j in range((n*n)):
                con=random()
                x2=self.nodos[j][0]
                y2=self.nodos[j][1]
                dis=sqrt(((y2-y1)**2)+((x2-x1)**2))
                if l==1:
                    if dis==1:
                        self.aristas.append((x1,y1,x2,y2))
                    else:
                        if con>prob:
                            self.aristas.append((x1,y1,x2,y2))
                else:
                    if l==2:
                        if dis==1:
                            self.aristas.append((x1,y1,x2,y2))
                        if dis==sqrt(2) or dis==2:
                            self.aristas.append((x1,y1,x2,y2))
                        else:
                            if con>prob:
                                self.aristas.append((x1,y1,x2,y2))
                            
                    else:
                        if l==3:
                            if dis==1:
                                self.aristas.append((x1,y1,x2,y2))
                            if dis==sqrt(2) or dis==2:
                                self.aristas.append((x1,y1,x2,y2))
                            if dis==3 or dis==1 or dis==sqrt(5):
                                self.aristas.append((x1,y1,x2,y2))
                            else:
                                if con>prob:
                                    self.aristas.append((x1,y1,x2,y2))
                        else:
                            if l==4:
                                if dis==1:
                                    self.aristas.append((x1,y1,x2,y2))
                                if dis==sqrt(2) or dis==2:
                                    self.aristas.append((x1,y1,x2,y2))
                                if dis==3 or dis==1 or dis==sqrt(5):
                                    self.aristas.append((x1,y1,x2,y2))
                                if dis==4 or dis==sqrt(2) or dis==sqrt(8) or dis==2 or dis==sqrt(10):
                                    self.aristas.append((x1,y1,x2,y2))
                                else:
                                    if con>prob:
                                        self.aristas.append((x1,y1,x2,y2))
                                                 
                            else:
                                if l==5:
                                    if dis==1:
                                        self.aristas.append((x1,y1,x2,y2))
                                    if dis==sqrt(2) or dis==2:
                                        self.aristas.append((x1,y1,x2,y2))
                                    if dis==3 or dis==1 or dis==sqrt(5):
                                        self.aristas.append((x1,y1,x2,y2))
                                    if dis==4 or dis==sqrt(2) or dis==sqrt(8) or dis==2 or dis==sqrt(10):
                                        self.aristas.append((x1,y1,x2,y2))
                                    if dis==5 or dis==sqrt(17) or dis==1 or dis==sqrt(13) or dis==sqrt(5) or dis==3:
                                        self.aristas.append((x1,y1,x2,y2))
                                    else:
                                        if con>prob:
                                            self.aristas.append((x1,y1,x2,y2))
        
        

            

    def ford_fulkerson(self): 
        self.s = self.nodos[0]
        self.t = self.nodos[k**2 - 1]
        print(self.s, self.t)
        if self.s == self.t:
            return 0
        maximo = 0
        self.f = dict()
        while True:
            aum = self.camino()
            if aum is None:
                break 
            incr = min(aum.values(), key = (lambda k: k[1]))[1]
            u = self.t
            while u in aum:
                v = aum[u][0]
                actual = self.f.get((v, u), 0) 
                inverso = self.f.get((u, v), 0)
                self.f[(v, u)] = actual + incr
                self.f[(u, v)] = inverso - incr
                u = v
            maximo += incr
        #with open("FulkersonCompleto.dat", "at") as archivo:
        print(maximo)
        return maximo

    def percolaNodos(self):
        self.auxIndice = []
        for h in range(2*k+5):
            self.auxnodo = []
            self.nodos2()
            self.ford_fulkerson()


    def percolaAristas(self):
        self.lqq = []
        for t in range(1,8):
            self.aristas2()
            self.ford_fulkerson()
            
    def graficar(self):
        with open("NoPercolar.plot","w") as archivo:
             print("set term pdf", file=archivo)
             print("set output 'hoy.pdf'", file=archivo)
             print("set xrange [2:13]", file=archivo)
             print("set yrange [1:12]", file=archivo)
             print("set pointsize .7", file=archivo)
             print("set size square", file=archivo)
             print("unset xtics", file=archivo)
             print("unset ytics", file=archivo)
             print("set key off", file=archivo)
             num=0
             for a in self.aristas:
                 (x1,y1,x2,y2)=a
                 print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 1".format(num+1,x1,y1,x2,y2),file=archivo)
                 num+=1
             print("plot 'nodos.dat' using 1:2 with points pt 7 lc 6", file=archivo)
             print("quit()",file=archivo)
                    
    def graficar(self):
        with open("Percolar.plot","w") as archivo:
             print("set term pdf", file=archivo)
             print("set output 'hoy.pdf'", file=archivo)
             print("set xrange [2:13]", file=archivo)
             print("set yrange [1:12]", file=archivo)
             print("set pointsize .7", file=archivo)
             print("set size square", file=archivo)
             print("unset xtics", file=archivo)
             print("unset ytics", file=archivo)
             print("set key off", file=archivo)
             num=0
             for a in self.aristas:
                 (x1,y1,x2,y2)=a
                 print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 1".format(num+1,x1,y1,x2,y2),file=archivo)
                 num+=1
             print("plot 'nodos2.dat' using 1:2 with points pt 7 lc 6", file=archivo)
             print("quit()",file=archivo)
                    
l=2
n=10
G=Grafo()
G.Nodos(n)
G.Aris(n, l)
G.graficar()
