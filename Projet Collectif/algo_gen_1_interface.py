from random import randint

#prendre L pair K pair et X pair ou X<L dans l'idéal, prob la proba de mutation en % ; N nombre itérations max
#glong et glarg c'est pour la taille de la grille mais n'a pas d'importance tant qu'on trace pas


# exemple d'appel : main([1,1,0],[1,11,0],10,10,10,10,2,1,2000)
def main(deb,fin,glong,glarg,L,K,X,prob,N): # orientation : 0 Haut , 1 Droite , 2 Bas , 3 Gauche 
    actions=['A','D','R','G'] # A est 0 ; D est 1 ; R est 2 ; G est 3 
    iter=0
    SA=init(L,K,actions,deb,fin,glong,glarg)# renvoie une liste de suite de commande aléatoire
    S=Sconvert(deb,SA,L,K)# transforme la suite en trajet
   # renvoie une distance de la liste de commande en argument
    LiDi=listdist(S,fin,L,K)
    distance=min(LiDi)
    if ((L-X)%2==1 and X<L):
        X=X+1
            
    while ((distance!=0) and (iter<N)):
        [S,SA]=nextgen(S,SA,deb,actions,LiDi,L,K,X,prob)
        LiDi=listdist(S,fin,L,K)
        distance=min(LiDi)
        iter+=1
    return [distance,S[LiDi.index(min(LiDi))],iter]
 
 
 
 
 
 
 
 ##fonction dist : prend un 3-uplet de fin du trajet et le 3-uplet d'arrivée  
def dist(coord,fin): # à modifier éventuellement si on ajoute obstacle 
    di=0
    diffH=abs(coord[0]-fin[0]) 
    diffV=abs(coord[1]-fin[1])
    if not(diffH==0 and diffV==0):
        di+=1
    di=di+diffH+diffV
    return di
    
## fonction init : renvoie L chemins de longueurs K générés aléatoirement dans l'espace des actions
def init(L,K,actions,deb,fin,glong,glar):
    S=[]
    C=[]
    for l in range (0,L):
        C=[]
        for k in range (0,K):
            C.append(actions[randint(0,3)])
        S.append(C[:])   
    return S
 
 ## fonction Sconvert : Convertit une chaine de L chemins de longueurs K de l'espace des actions dans l'espace des coordonées
def Sconvert(deb,SA,L,K):
    S=[]
    C=[]
    D=deb[:]
    for l in range (0,L):
        C=[]
        for k in range (0,K):
            if k==0:
                C.append(mouv(D,SA[l][k]))
            else :
                C.append(mouv(C[k-1],SA[l][k]))              
        S.append(C[:])
    return S
 
## fonction mouv : renvoie la coordonnée suivante après avoir effectuée l'action sur la coordonnée d'entrée    
def mouv(coord,action):
    cord=coord[:]
    if action=='A':
        if cord[2]==0:
            cord[1]+=1
        elif cord[2]==1:
            cord[0]+=1
        elif cord[2]==2:
            cord[1]+=-1
        elif cord[2]==3 :
            cord[0]+=-1 
    
    elif action=='R':
        if cord[2]==0:
            cord[1]+=-1
        elif cord[2]==1:
            cord[0]+=-1
        elif cord[2]==2:
            cord[1]+=1
        elif cord[2]==3 :
            cord[0]+=1         
    
    elif action=='D':
        cord[2]+=1
        cord[2]=cord[2]%4
    elif action=='G' :
        cord[2]+=-1
        cord[2]=cord[2]%4
    return cord
    
## à faire mais je sais pas trop comment     
def tracer(S):
    return

##fonction nextgen : calcule les chaines de chemins suivants : Mise à jour des chemins après selection, croisement et mutation ( S chemin espace coordonée , SA chemin espace actions )
def nextgen(S,SA,deb,actions,LiDi,L,K,X,prob):
    Res=[]
    SelA=select(S,SA,LiDi,X)
    CroisA=crois(SA,L,K,X)
    SelA.extend(CroisA)
    SelA=muta(SelA,prob,actions,L,K)
    Sel=Sconvert(deb,SelA,L,K) 
    return [Sel,SelA]

## fonction select : choisir et renvoie les X meilleurs chemins en terme de distance à l'arrivée ; les chemins renvoyés sont dans l'espace des actions
def select(S,SA,LiDi,X):
    SelA=[]
    Copy=LiDi[:]
    for x in range (0,X):
        ind=(Copy.index(min(Copy)))
        SelA.append(SA[ind])
        Copy[ind]=100
    return SelA

## fonction crois : On crée et renvoie L-X chemins spaciaux en mixant les L chemins
def crois(SA,L,K,X): #croisement uniforme
    copy=SA[:]
    Cr=[]
    for x in range (0,(L-X)//2):

        rd1=randint(0,L-1)
        rd2=randint(0,L-1)
        while (rd2==rd1):
            rd2=randint(0,L-1)
        L1=copy[rd1]
        L2=copy[rd2]
        MA1=L1[0:(K+1)//2]
        MA2=L1[(K+1)//2:K]
        MB1=L2[0:(K+1)//2]
        MB2=L2[(K+1)//2:K]
        MA1.extend(MB1)
        MB1.extend(MA2)
        Cr.append(MB1)
        Cr.append(MA1)  
    return  Cr

## fonction muta : sur chaque action : proba prob de la remplacer par une des 4 actions au hasard
def muta(S,prob,actions,L,K):
    if prob==0:
        return S
    fact=1
    while (prob<=1):
        prob=prob*10
        fact=fact*10
    
    for l in range (0,L):
        for k in range (0,K):
            rd=randint(0,100*fact)
            if rd<prob:
                al=randint(0,3)
                S[l][k]=actions[al]
    return S

## fonction listdist : renvoie une liste de longueur L correspondant pour chaque chemin : à la distance entre la fin du chemin et de l'arrivée
def listdist(S,fin,L,K):
    List=[]
    for x in range(0,L):
        res=dist([S[x][K-1][0],S[x][K-1][1],S[x][K-1][2]],fin)
        List.append(res)
    return List
    
  ##        
    
  ##
  ##
  ##
  ##
  
  
  
  

from tkinter import *
from random import randrange
 
# --- définition des fonctions gestionnaires d'événements : ---
def maincmd():
    L=int(Linput.get())
    print(type(L))
    K=int(Kinput.get())
    N=int(Ninput.get())
    P=int(Pinput.get())
    X=int(Xinput.get())
    deb=[int(debinputx.get()),int(debinputy.get()),int(debinputor.get())]
    fin=[int(fininputx.get()),int(fininputy.get()),int(fininputor.get())]
    glong=int(glonginput.get())
    glarg=int(glarginput.get())
    Res=main(deb,fin,glong,glarg,L,K,X,P,N)
    [distance,Cheminfinal,iter]=Res
    
    Itervarlabel=Label(text=iter)
    Itervarlabel.place(x=1330,y=500)
    
    Cheminvarlabel=Label(text=Cheminfinal)
    Cheminvarlabel.place(x=1000,y=550)
    
    Distvarlabel=Label(text=distance )
    Distvarlabel.place(x=1480,y=600)
    
#------ Programme principal -------
 
# les variables suivantes seront utilisées de manière globale :
                          # couleur de la ligne
 
# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=800,width=800)
can1.place(x=0,y=0)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)


 
Llabel=Label(text='Choisir le nombre de chemins à chaque génération  L=')
Llabel.place(x=900, y=100)
Linput=Entry(width=3)
Linput.place(x=1270,y=100)

Klabel=Label(text='Choisir le nombre d action d un chemin                     K=')
Klabel.place(x=900, y=120)
Kinput=Entry(width=3)
Kinput.place(x=1270,y=120)
 
Nlabel=Label(text='Choisir le nombre maximum d itérations                   N=')
Nlabel.place(x=900, y=140)
Ninput=Entry(width=5)
Ninput.place(x=1270,y=140)
 
Plabel=Label(text='Choisir la probabilité de mutation d une action         P=')
Plabel.place(x=900, y=160)
Pinput=Entry(width=3)
Pinput.place(x=1270,y=160) 

Xlabel=Label(text='Choisir combien de meilleur chemin à garder            X=')
Xlabel.place(x=900, y=180)
Xinput=Entry(width=3)
Xinput.place(x=1270,y=180) 

deblabel=Label(text='Choisir les coordonnées de départ       x=           y=          orientation=            (0 haut; 1 droite ; 2 bas ; 3 gauche)')
deblabel.place(x=900, y=220)
debinputx=Entry(width=3)
debinputx.place(x=1180,y=220) 
debinputy=Entry(width=3)
debinputy.place(x=1240,y=220) 
debinputor=Entry(width=3)
debinputor.place(x=1360,y=220) 

finlabel=Label(text='Choisir les coordonnées d arrivée         x=           y=          orientation=            (0 haut; 1 droite ; 2 bas ; 3 gauche)')
finlabel.place(x=900, y=250)
fininputx=Entry(width=3)
fininputx.place(x=1180,y=250) 
fininputy=Entry(width=3)
fininputy.place(x=1240,y=250) 
fininputor=Entry(width=3)
fininputor.place(x=1360,y=250) 

glonglabel=Label(text='Choisir la hauteur en case de la grille                 glong=')
glonglabel.place(x=900, y=280)
glonginput=Entry(width=3)
glonginput.place(x=1270,y=280) 

glarglabel=Label(text='Choisir la longueur en case de la grille                glarg=')
glarglabel.place(x=900, y=310)
glarginput=Entry(width=3)
glarginput.place(x=1270,y=310) 

Main = Button(text='Simuler',command=maincmd,width=50)
Main.place(x=1000,y=400)

Iterlabel=Label(text='Le nombre d itération a été de :')
Iterlabel.place(x=1100,y=500)


Cheminlabel=Label(text='Le chemin a été : ')
Cheminlabel.place(x=850,y=550)

Distlabel=Label(text='La distance entre la fin du trajet et de l arrivée est de :' )
Distlabel=Distlabel.place(x=1100,y=600)


fen1.mainloop()              # démarrage du réceptionnaire d'événements
 
fen1.destroy()              
  
  
  
  
  
  
        
        
        
        