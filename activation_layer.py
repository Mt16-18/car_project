from layer import Layer

#inherit from base class Layer
class ActivationLayer(Layer):
    def __init__(self, activation):
        self.activation = activation
    #return the activated input
    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = self.activation(self.input)
        return self.output

    def genetic_correction(self,other_network,k,q):
        return(other_network)

        #returns input_error = dE/dS for a given output_error= dE/dY
        #learning_rate is not use because is no "learnable" paraleteres