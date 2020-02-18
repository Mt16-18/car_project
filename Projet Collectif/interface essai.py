
# Petit exercice utilisant la bibliothèque graphique Tkinter
 
from tkinter import *
from random import randrange
 
# --- définition des fonctions gestionnaires d'événements : ---
def maincmd():
    L=Linput.get()
    K=Kinput.get()
    N=Ninput.get()
    P=Pinput.get()
    X=Xinput.get()
    deb=[debinputx.get(),debinputy.get(),debinputor.get()]
    fin=[fininputx.get(),fininputy.get(),fininputor.get()]
    glong=glonginput.get()
    glarg=glarginput.get()
#    [distance,Cheminfinal,iter]=main
    print(rd)
    
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





fen1.mainloop()              # démarrage du réceptionnaire d'événements
 
fen1.destroy()              