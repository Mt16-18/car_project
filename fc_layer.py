from layer import Layer
import numpy as np
from random import *
# inherit from base class Layer
class FCLayer(Layer):
    #input_size = number of input neurons
    #output_size = number of output neurons
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(input_size, output_size) - 0.5
        self.bias = np.random.rand(1,output_size) -0.5
        self.input_size= input_size
        self.output_size = output_size
    #return output for a given input
    def forward_propagation(self, input_data): #permet de passer de la première couche à la dernière
        self.input = input_data  #donner d'entrée
        self.output = np.dot(self.input, self.weights) +self.bias #donnée sortie de la couche
        return self.output #renvoie sortie de la couche
    def genetic_correction(self,other_network,k,q):
        compt = 0
        for layer in other_network.layers:
            if compt == k: #si on est à la même couche du réqeau de neurone, on mélange les poids
                self.weights[0:int(self.input_size/2)] = layer.weights[0:int(self.input_size/2)]
                self.bias[0:int(self.output_size/2)] = layer.bias[0:int(self.output_size/2)]

                ##mutation
                while(random()<q): #mutation des poids, q arbitraire
                    i = randint(0,self.input_size-1)
                    j = randint(0,self.output_size-1)
                    self.weights[i][j] = uniform(-10,10) #nombre aléatoire (mutation)
                while(random()<q): #mutation des biais, q arbitraire
                    i = randint(0,self.output_size-1)
                    self.bias [0][i] = uniform(-10,10) #nombre aléatoire (mutation)
            compt+=1
        return 0
