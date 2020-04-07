from random import *
import numpy as np
from fc_layer import FCLayer
# Network permet de faire le lien entre toutes les couches du réseau de neurone
class Network:
    def __init__(self):
        self.layers = []
        self.loss = None

    #add layer to network
    def add(self , layer):
        self.layers.append(layer)

    #set loss to use

    def use(self, loss):
        self.loss = loss

    #predict(self, input_data):
##
    def predict(self,input_data):
        #sample dimension first
        samples = len(input_data)
        result = []
        #run network over all samples
        for i in range(samples):
            #forward propagation
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)
        return result
        #train the network
##fit est une méthode permettant créer un nouvel individu en en fusionant 2 anciens
    def fit(self, resultat,q):
        taille = len(resultat)
        aleatoire = randint(0,int(taille/2))

        other_network=resultat[aleatoire][1] #choix du la femme
        k = 0
        for layer in self.layers: #pour toute les couches du réseau
            layer.genetic_correction(other_network,k,q) #on change les valeurs en combinant self et other_network
            k+=1

