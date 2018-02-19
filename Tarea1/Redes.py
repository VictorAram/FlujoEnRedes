from random import uniform
import math
n=10
nodos=[]
Eu=[]
aristas=[]
with open ("nodos.dat", "w") as crear:
    aux=1
    for t in range(n):
        x=uniform(1,30)
        y=uniform(1,30)
##        print("set style data point".format(aux, p), file=crear)
        nodos.append((x,y))
        print(x,y,file=crear)
t=0
f=0
matriz = []
for t in range(n):
    Eu.append([])
    for f in range(n):
        Eu[t].append(None)
        
t=0
f=0
for t in range(n):
    x1=nodos[t][0]
    y1=nodos[t][1]
    for f in range(n):
        g1=nodos[f][0]
        g2=nodos[f][1]
        Eu[t][f]=math.sqrt(((g2-y1)**2)+((g1-x1)**2))
        if Eu[t][f]<10:
            aristas.append((x1,y1,g1,g2))


with open("tarea1.plot","w") as archivo:
    print("set term png", file=archivo)
    print("set output 'grafica.png'", file=archivo)
    print("set xrange [0:30]", file=archivo)
    print("set yrange [0:30]", file=archivo)
    print("set pointsize 3", file=archivo)
    print("set size square", file=archivo)
    print("set key off", file=archivo)
    num=1
    for a in aristas:
        (x1,y1,x2,y2)=a
        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 3".format(num,x1,y1,x2,y2),file=archivo)
        num+=1
    print("show arrow", file=archivo)
    print("plot 'nodos.dat' using 1:2 with points pt 7", file=archivo)
    print("quit()",file=archivo) 
