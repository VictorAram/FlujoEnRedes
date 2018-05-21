from random import uniform
from random import randint
from random import random
from math import sqrt

class Grafo:
    def __init__(self):
        self.nodos=[]
        self.aristas=[]
        self.nodos2=[]
        self.aristas2=[]
        self.doc={}

    def Nodos (self, n):
        with open("nodos.dat","w") as crear:
            for t in range(n):
                x=randint(2,12)
                y=randint(2,12)
                self.nodos.append((x,y))
                print(x,y, file=crear)

    def Aris(self):
        prob=0.85
        for (x1,y1) in self.nodos:
            for (x2,y2) in self.nodos:
                ti=random()
                Ton=randint(2,20)
                if (x1,y1)!=(x2,y2):
                    dis=sqrt(((y2-y1)**2)+((x2-x1)**2))
                    Df=(x2,y2,x1,y1)in self.doc
                    if dis<=15 and ti>prob:
                        if Df is False:
                            self.doc.setdefault((x1,y1,x2,y2),Ton)
                            self.aristas.append((x1,y1,x2,y2))

###############################################################

    def Nod(self,n):
        h=80
        w=1
        for i in range(n-2):
            for j in range(w):
                for (x1,y1) in self.nodos:
                    for (x2,y2) in self.nodos:
                        q= (x1,y1,x2,y2)in self.doc
                        if q == True: 
                            gh=self.doc[(x1,y1,x2,y2)]
                            if gh<h:
                                h=gh
                                A1=x1
                                B1=y1
                                A2=x2
                                B2=y2
                print(A1,B1,A2,B2,h)
                for (x3,y3) in self.nodos:
                    print(x3,y3)
                    f1=(A1+A2)/2
                    f2=(B1+B2)/2
##                            #para el nodo 1
                    k1=(A1,B1,x3,y3)in self.doc
                    k2=(x3,y3,A1,B1)in self.doc
                    if k1==True:
                        r1=self.doc[(A1,B1,x3,y3)]
                        print(r1)
                        del self.doc[(A1,B1,x3,y3)]
                    else:
                        r1=0
                    if k2==True:
                        r3=self.doc[(x3,y3,A1,B1)]
                        print(r3)
                        del self.doc[(x3,y3,A1,B1)]
                    else:
                        r3=0
                    R=r1+r3
##            #para el nodo 2
                    v1=(A2,B2,x3,y3)in self.doc
                    v2=(x3,y3,A2,B2)in self.doc
                    if v1==True:
                        c1=self.doc[(A2,B2,x3,y3)]
                        del self.doc[(A2,B2,x3,y3)]
                    else:
                        c1=0
                    if v2==True:
                        c2=self.doc[(x3,y3,A2,B2)]
                        del self.doc[(x3,y3,A2,B2)]
                    else:
                        c2=0
                    C=c1+c2
                    Q=R+C
                    if Q!=0:
                        self.doc.setdefault((f1,f2,x3,y3),Q)
            self.nodos.remove((A1,B1))
            self.nodos.remove((A2,B2))
            

            




                    
    def graficar(self):
        with open("Tar6.plot","w") as archivo:
             print("set term pdf", file=archivo)
             print("set output 'T6.pdf'", file=archivo)
             print("set xrange [1:13]", file=archivo)
             print("set yrange [1:13]", file=archivo)
             print("set pointsize .7", file=archivo)
             print("set size square", file=archivo)
             #print("unset xtics", file=archivo)
             #print("unset ytics", file=archivo)
             print("set key off", file=archivo)
             num=0
             for a in self.aristas:
                 (x1,y1,x2,y2)=a
                 print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 1".format(num+1,x1,y1,x2,y2),file=archivo)
                 num+=1
             print("plot 'nodos.dat' using 1:2 with points pt 7 lc 6", file=archivo)
             print("quit()",file=archivo)
                    

n=10

G=Grafo()
G.Nodos(n)
G.Aris()
G.Nod(n)
G.graficar()
