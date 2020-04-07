import numpy as np
from random import *
from network import Network
from fc_layer import FCLayer
from activation_layer import ActivationLayer
from activations import tanh
from losses import mse
from copy import deepcopy

## fonction de tri
def quicksort(t):
    if t == []:
        return []
    else:
        pivot = t[0]
        t1=[]
        t2=[]
        if(len(t)>1):
            for k in range(1,len(t)):
                if t[k][0]<pivot[0]:
                    t1.append(t[k])
                else:
                    t2.append(t[k])
        return quicksort(t1) + [pivot] + quicksort(t2)


## init
population = 10 #nombre total de cas tester en meme temps
nombre = 1000 #nombre de géneration
q = 0.3 #facteur de mutation (entre 0 et 1)

x_train = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]]) #ce qui est en entrée
##init des reseaux de neurones aléatoirement
liste =[]
for k in range(0 ,population) :#on crée "population" réseaux de neurones
    liste.append([0,Network()])
    liste[-1][1].add(FCLayer(2,3))# construction des couches
    liste[-1][1].add(ActivationLayer(tanh)) #choix fonction d'activation
    liste[-1][1].add(FCLayer(3,3))
    liste[-1][1].add(ActivationLayer(tanh))
    liste[-1][1].add(FCLayer(3,1))
    liste[-1][1].add(ActivationLayer(tanh))
    n=0
while(n<nombre): #tant que l'on n'est pas à la "nombre"ème génerations
    n+=1
    for k in range(0,population): #pour tout les réseaux de neurones
        y_trouve = []
        y_voulu = []
        for x in x_train : #on met les 4 entrées
            y=liste[k][1].predict(x)#on teste les reseaux de neurones
            y_attendu = x[0][0]^x[0][1] #la valeur que l'on doit avoir
            y_voulu.append(y_attendu) #on met les resultats dans un tableau
            y_trouve.append(y)
        J = np.mean(np.power(np.subtract(np.transpose(y_trouve),y_voulu), 2)) #critère de convergence
        liste[k][0]=J #sauvegarde du critère
        #print("J=",J)
        #print(liste)
    liste = quicksort(liste) #on tri les réesaux suivant la valeurs de leur critère
    print("J= ", liste[0][0])
    liste2 = deepcopy(liste) #copie de tout les réseaux (on manipule des objets, il faut faire attention)
    liste3 = deepcopy(liste)
    for k in range(1,population,2):
        liste[k-1][1] = deepcopy(liste2[int(k/2)][1])  #on reprend les 50% meilleurs de l'ancienne géneration et on les met dans la nouvelle
        liste2[int(k/2)][1].fit(liste3,q)#on crée de nouveaux génome s
        liste[k][1] = deepcopy(liste2[int(k/2)][1]) #on les met dans la nouvelle population
out= liste[0][1].predict(x_train) #affichage final des resultat donnés par le meilleur réseau trouvé
print(out)

