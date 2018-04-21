from math import sqrt, ceil, sin, cos, pi, floor
from random import randint, uniform, random
import time, random

class Grafo:
    def __init__(self):
        self.dis=dict()
        self.vecinos=dict()
        self.aristas=dict()
        self.nodos=[]
        #self.pos=dict()

    #nodos al rededor del centro
    def agrega(self, v, c, rad, ang):
        with open("Nodos.dat", "w") as crear:
            for n in range(1, v+1):
                x = rad*cos(ang*n) + c[0]
                y = rad*sin(ang*n) + c[1]
                self.nodos.append((x,y))
                print(x, y, file = crear)
                if not (x, y) in self.vecinos:
                    self.vecinos[(x,y)] = []

    #conectaremos nodos correspondientes en k
    def conecta(self, k):
        for r in range(1,k+1):
            for j in range(0,v):
                a = self.nodos[j]
                b = self.nodos[j-r]
                self.aristas[(a,b)] = self.aristas[(b,a)] = r
                self.vecinos[a].append(b)
                self.vecinos[b].append(a)

    def grafos(self):
        with open("tareaT4.plot","w") as archivo:
            print("set term png", file=archivo)
            print("set output 'tarea4.png'", file=archivo)
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
                p = self.aristas[key]
                print("set arrow {:d} from {:f},{:f} to {:f}, {:f} nohead lw 1".format(num+1,x1,y1,x2,y2),file=archivo)
                num+=1
            print("show arrow", file=archivo)
            print("plot 'Nodos.dat' using 1:2 with points pt 7", file=archivo)
            print("quit()", file=archivo)

v=10
k=3
c = (0.5, 0.5)
rad = 0.4
ang = (360/v)*(pi/180)
G=Grafo()
G.agrega(v, c, rad, ang)
G.conecta(k)
G.grafos()


      
