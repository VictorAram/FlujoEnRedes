from random import uniform
from random import random
from math import sqrt

class Grafo:
    def __init__(self):
        self.nodos=[]
        self.aristas=[]

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
        prob=0.98
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
                    if l==2:
                        if dis==1:
                            self.aristas.append((x1,y1,x2,y2))
                        m=sqrt(2)
                        if dis==m or dis==2:
                            if con>prob:
                                self.aristas.append((x1,y1,x2,y2))
                            
                    else:
                        if l==3:
                            if dis==1:
                                self.aristas.append((x1,y1,x2,y2))
                            if dis==sqrt(2) or dis==2:
                                if con>prob:
                                    self.aristas.append((x1,y1,x2,y2))
                            if dis==3 or dis==1 or dis==sqrt(5):
                                if con>prob:
                                    self.aristas.append((x1,y1,x2,y2))
                        else:
                            if l==4:
                                if dis==1:
                                    self.aristas.append((x1,y1,x2,y2))
                                if dis==sqrt(2) or dis==2:
                                    if con>prob:
                                        self.aristas.append((x1,y1,x2,y2))
                                if dis==3 or dis==1 or dis==sqrt(5):
                                    if con>prob:
                                        self.aristas.append((x1,y1,x2,y2))
                                if dis==4 or dis==sqrt(2) or dis==sqrt(8) or dis==2 or dis==sqrt(10):
                                    if con>prob:
                                        self.aristas.append((x1,y1,x2,y2))
                                                 
                            else:
                                if l==5:
                                    if dis==1:
                                        self.aristas.append((x1,y1,x2,y2))
                                    if dis==sqrt(2) or dis==2:
                                        if con>prob:
                                            self.aristas.append((x1,y1,x2,y2))
                                    if dis==3 or dis==1 or dis==sqrt(5):
                                        if con>prob:
                                            self.aristas.append((x1,y1,x2,y2))
                                    if dis==4 or dis==sqrt(2) or dis==sqrt(8) or dis==2 or dis==sqrt(10):
                                        if con>prob:
                                            self.aristas.append((x1,y1,x2,y2))
                                    if dis==5 or dis==sqrt(17) or dis==1 or dis==sqrt(13) or dis==sqrt(5) or dis==3:
                                        if con>prob:
                                            self.aristas.append((x1,y1,x2,y2))
        
        
##    def Aris(self,n):
##        for j in range(n):
##            for g in range(n):
##                h1=g+(j*n)
##                u=j+1
##                h2=(u*n)+g
##                x1=self.nodos[h1][0]
##                y1=self.nodos[h1][1]
####                x2=self.nodos[j+1][0]
####                y2=self.nodos[j+1][1]
####                self.aristas.append((x1,y1,x2,y2))
##                x3=self.nodos[h2][0]
##                y3=self.nodos[h2][1]
##                self.aristas.append((x1,y1,x3,y3))
##
##
            
            
    def graficar(self):
        with open("hoy.plot","w") as archivo:
             print("set term pdf", file=archivo)
             print("set output 'hoy.pdf'", file=archivo)
             print("set xrange [0:13]", file=archivo)
             print("set yrange [0:13]", file=archivo)
             print("set pointsize .7", file=archivo)
             print("set size square", file=archivo)
             print("set key off", file=archivo)
             num=0
             for a in self.aristas:
                 (x1,y1,x2,y2)=a
                 print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head lw 1".format(num+1,x1,y1,x2,y2),file=archivo)
                 num+=1
             print("plot 'nodos.dat' using 1:2 with points pt 7 lc 6", file=archivo)
             print("quit()",file=archivo)
                    

l=5
n=10
G=Grafo()
G.Nodos(n)
G.Aris(n, l)
G.graficar()
