#16 Feed Forward Neural Network

import numpy as np
from scipy.special import expit

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_hidden = np.zeros((1, self.hidden_size))
        
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_output = np.zeros((1, self.output_size))
        
    def sigmoid(self, x):
        return expit(x)
    
    def forward(self, inputs):
        # Calculate hidden layer activations
        hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        hidden_output = self.sigmoid(hidden_input)
        
        # Calculate final output
        output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
        predicted_output = self.sigmoid(output_input)
        
        return predicted_output

# Take user input for network parameters
input_size = int(input("Enter input size: "))
hidden_size = int(input("Enter hidden size: "))
output_size = int(input("Enter output size: "))

# Create a neural network instance
nn = NeuralNetwork(input_size, hidden_size, output_size)

# Take user input for input data
num_samples = int(input("Enter the number of input samples: "))
inputs = []
for _ in range(num_samples):
    input_data = [float(x) for x in input("Enter input data (space-separated values): ").split()]
    inputs.append(input_data)

# Perform forward pass
for input_data in inputs:
    predicted_output = nn.forward(input_data)
    print(f"Input: {input_data}, Predicted Output: {predicted_output}")
