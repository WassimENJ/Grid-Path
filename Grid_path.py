# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:28:43 2023


"""

# Wassim 

from random import *
from collections import deque
from turtle import *

# partie 1
def initialisergrille(n,m):

    l = [[[0, 0, 0, 0] for i in range(n)] for j in range(m)]
    print(l)
    for i in l:#initialiser
         for j in i:
             for k in range(len(j)):
                       j[k]=randint(15,20)

    for i in l:# affichage
        for j in i:
            print(j,end=" ")
        print()
    # egalisation des colognnes partagées entres les cases
    for i in range(n):
        for j in range(m-1,0,-1):
            l[i][j][3]=l[i][j-1][1]
    #egalisation des lignes partagées
    for i in range(n-1,0,-1):
        for j in range(m):
            l[i][j][0]=l[i-1][j][2]
    print("#"*100)
    for i in l:
        for j in i:
            print(j, end=" ")
        print()
    return l

def desiner_case(c,j,s):
    pensize(c[0])
    forward(150)  # Déplace la tortue de 150 unités vers l'avan
    right(90)  #
    pensize(c[1])
    forward(150)  # Déplace la tortue de 150 unités vers l'avan
    right(90)  #
    pensize(c[2])
    forward(150)  # Déplace la tortue de 150 unités vers l'avan
    right(90)  #
    pensize(c[3])
    forward(150)  # Déplace la tortue de 150 unités vers l'avan
    right(90)
    pensize(c[0])
    forward(150)  # Déplace la tortue de 150 unités vers l'avan
    if j == s:
        pensize(0)
        setx(-300.0)
        sety(ycor()-150.0)

def desiner_grille(G):
    for i in range(len(G)):
        for j in range(len(G[0])):
            desiner_case(G[i][j],j,len(G[0])-1)

            
#Partie 2

def parcoursgrille2(G):
    f=deque()
    for i in range(len(G)):
        for j in range(len(G[0])):
            if (i!=len(G)-1) or (j!=len(G[0])-1):
                if j == len(G[0]) - 1:
                    f.append([G[i][j][2],(i,j),(i+1,j)])
                elif i == len(G)-1:
                    f.append([G[i][j][1],(i,j),(i,j+1)])
                else:
                    f.append([G[i][j][1],(i,j),(i,j+1)])
                    f.append([G[i][j][2], (i, j), (i + 1, j)])
    return f
def aux_voisine(f,i,j):
    l=[]
    for x in f:
        if i==x[1][0] and j == x[1][1]:
            l.append(x)
    return l
def chemins_glt_rec2(f,i,j,c):
    if i!=f[-1][-1][0] or j != f[-1][-1][1]:
        v=aux_voisine(f,i,j)
        if len(v)>1:
            if v[0][0]>v[1][0]:
                c+=v[1][0]
                return [(i,j)]+chemins_glt_rec2(f,v[1][2][0],v[1][2][1],c)
            c+=v[0][0]
            return [(i,j)]+chemins_glt_rec2(f,v[0][2][0],v[0][2][1],c)
        c+=v[0][0]
        return [(i,j)]+chemins_glt_rec2(f,v[0][2][0],v[0][2][1],c)
    print("Le cout minimal suivant algo glouton est : ",c)

    return [(i,j)]


#partie 3
def initialiser_partie3(m,n):
    l = [[[0, 0, 0, 0,False] for i in range(m)] for j in range(n)]
    print(l)
    for i in l:  # initialiser
        for j in i:
            for k in range(len(j)-1):
                j[k] = randint(1,20)

    for i in l:  # affichage
        for j in i:
            print(j, end=" ")
        print()
    # egalisation des colognnes partagées entres les cases
    for i in range(m):
        for j in range(n - 1, 0, -1):
            l[i][j][3] = l[i][j - 1][1]
    # egalisation des lignes partagées
    for i in range(m -1, 0, -1):
        for j in range(n):
            l[i][j][0] = l[i - 1][j][2]
    l[m-1][n-1][3]=l[m-1][n-2][1]

    print("-" * 200)
    for i in l:
        for j in i:
            print(j, end=" ")
        print()
    return l
def chemins_glt_rec_partie3(f,i,j,G):
    G[0][0][4]=True
    if i!=f[-1][-1][0] or j != f[-1][-1][1]:
        v=aux_voisine(f,i,j)
        if len(v)>1:
            if v[0][0]>v[1][0]:
                G[v[1][2][0]][v[1][2][1]][0]=0
                G[i][j][2]=0
                G[v[1][2][0]][v[1][2][1]][4] = True
                return [(i,j)]+chemins_glt_rec_partie3(f,v[1][2][0],v[1][2][1],G)
            else:
                G[v[0][2][0]][v[0][2][1]][3] = 0
                G[i][j][1] = 0
                G[v[0][2][0]][v[0][2][1]][4] =True
                return [(i,j)]+chemins_glt_rec_partie3(f,v[0][2][0],v[0][2][1],G)
        else:
            if i==len(G)-1:
                G[v[0][2][0]][v[0][2][1]][3] = 0
                G[i][j][1] = 0
                G[v[0][2][0]][v[0][2][1]][4] = True
            else:
                G[v[0][2][0]][v[0][2][1]][0] = 0
                G[i][j][2] = 0
                G[v[0][2][0]][v[0][2][1]][4] = True
            return [(i,j)]+chemins_glt_rec_partie3(f,v[0][2][0],v[0][2][1],G)
    return [(i,j)]

def desiner_case(c,j,s):
    for i in range(len(c)):
        if i == len(c)-1:
            if c[0]!=0:
                pensize(c[0])
                forward(150)
            else:
                pencolor('red')
                forward(150)
                pencolor('black')
        else:
            if c[i]==0:
                pencolor('red')
                forward(150)  # Déplace la tortue de 150 unités vers l'avan
                right(90)  #
                pencolor('black')
            else:
                pensize(c[i])
                forward(150)  # Déplace la tortue de 150 unités vers l'avan
                right(90)  #
    if j == s:
        penup()
        hideturtle()
        setx(-300.0)
        sety(ycor()-150)
        showturtle()
        pendown()

def desiner_grille(G):
    speed(1500)
    penup()
    hideturtle()
    setx(-300.0)
    sety(300.0)
    showturtle()
    pendown()
    pencolor('black')
    t = len(G)
    for i in range(len(G)):
        for j in range(len(G[0])):
            desiner_case(G[i][j],j,len(G[0])-1)



# g = initialiser_partie3(3, 3)
# f= parcoursgrille2(g)
# print(f)
# print(chemins_glt_rec_partie3(f, 0, 0, g))

# for i in g:
#     for j in i:
#         print(j, end=" ")
#     print()

# desiner_grille(g)





#Partie4



def chemins_rec2(x,y):
    if x == 0 and y == 0: #arrivée au point, 1 chemin de plus
        return 1
    else:
#       on peut arriver de 3 manières d'un point situé en bas à gauche
        if x != 0 and y != 0:
            return chemins_rec2(x-1,y) + chemins_rec2(x,y-1) 
#       mais que d'une seule manière d'un point situé sur un axe
        if x == 0 and y != 0:
            return chemins_rec2(x,y-1) 
        if x != 0 and y == 0:
            return chemins_rec2(x-1,y)

def chemins_bonus_aux(f,i,j,c):
    if i!=f[-1][-1][0] or j != f[-1][-1][1]:
        v=aux_voisine(f,i,j)
        if len(v)>1:
            r = randint(0, 1)
            c+=v[r][0]
            return [v[r][2]]+chemins_bonus_aux(f, v[r][2][0], v[r][2][1], c)
        else:
            c+=v[0][0]
            return [v[0][2]]+chemins_bonus_aux(f, v[0][2][0], v[0][2][1], c)
    return [c]
   
    
def chemins_bonus(n,f):
    L=[]
    while len(L)<n:
        ch = [(0,0)]+chemins_bonus_aux(f, 0, 0, 0)
        if ch not in L:
            L.append(ch)
    L.sort(key=lambda x:x[-1])
    print("Le cout minimal suivant algo wassim & abdeladim est  : ",L[0].pop())
    return L[0]


g = initialiser_partie3(10, 10)
f = parcoursgrille2(g)
n = chemins_rec2(len(g)-1, len(g[0])-1)
res = chemins_bonus(n, f)
print(res)
print(chemins_glt_rec2(f, 0, 0, 0))


    


 

    
    

