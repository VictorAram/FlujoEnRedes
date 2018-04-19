from math import sqrt, ceil, sin, cos, pi, floor
from random import randint, uniform, random
import time, random

class Grafo:
    def __init__(self):
        self.dis=dict()
        self.vecinos=dict()
        self.aristas=dict()
        self.nodos=[]
        self.pos=dict()

    #nodos al rededor del centro
    def agrega(self, v):
        with open("Nodos.dat","w") as crear:
            c=(0.5, 0.5)
            ra=0.3
            angulo=2*pi/v #partición de circunferencia correspondiente al No. de nodos
            self.pos[v] = (c[0]+(0.4 * cos(angulo * v)), c[1]+(0.4 * sin(angulo * v)))
            x=self.pos[v][0]
            y=self.pos[v][1]
##            for n in range(1,u+1):
##                x= 0.3* (cos(ang*10)) + 0.5
##                y= 0.3* (sin(ang*10)) + 0.5
            self.nodos.append((x,y))
            print(x, y, file = crear)
            if not (x,y) in self.vecinos:
                self.vecinos[(x,y)]=[]

    #conectaremos nodos correspondientes en k        
    def conecta(self, k, v):
        for q in range(1,k+1):
            for j in range(0,v):
                m=self.nodos[j]
                n1=self.nodos[j-q]
                self.aristas[(m,n1)]=self.aristas[(n1,m)]=q
                self.vecinos[m].append(n1)
                self.vecinos[n1].append(m)


    def grafos(self):
        with open("tarea4.plot","w") as archivo:
            print("set term pdf", file=archivo)
            print("set output 'tarea4.pdf'", file=archivo)
            print("set xrange [-0.1:1.1]", file=archivo)
            print("set yrange [-0.1:1.1]", file=archivo)
            print("set pointsize 1", file=archivo)
            print("set size square", file=archivo)
            print("set key off", file=archivo)
            num=0
            for key in self.aristas:
                x1= key[0][0]
                y1= key[0][1]
                x2= key[1][0]
                y2= key[1][1]
                print("set arrow{:d} from {:f},{:f} to {:f}, {:f} nohead".format(num+1,x1,y1,x2,y2), file =archivo)
                num+=1
            print("show arrow", file=archivo)
            print("plot 'tarea4.dat' using 1:2 with points pt 7", file=archivo)
            print("quit()", file=archivo)

v=10
k=1
G=Grafo()
G.agrega(v)
G.conecta(k,v)
G.grafos()











            
            
