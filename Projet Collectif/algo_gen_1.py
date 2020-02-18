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
        
        
        
        
        
        