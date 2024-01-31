import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases with random values
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))

    def forward(self, inputs):
        # Perform forward pass
        self.hidden_layer_activation = sigmoid(np.dot(inputs, self.weights_input_hidden) + self.bias_hidden)
        self.output = sigmoid(np.dot(self.hidden_layer_activation, self.weights_hidden_output) + self.bias_output)
        return self.output

    def train(self, inputs, targets, learning_rate, epochs):
        for epoch in range(epochs):
            # Forward pass
            self.forward(inputs)

            # Calculate errors
            output_errors = targets - self.output

            # Backpropagation
            output_delta = output_errors * sigmoid_derivative(self.output)
            hidden_errors = output_delta.dot(self.weights_hidden_output.T)
            hidden_delta = hidden_errors * sigmoid_derivative(self.hidden_layer_activation)

            # Update weights and biases
            self.weights_hidden_output += self.hidden_layer_activation.T.dot(output_delta) * learning_rate
            self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
            self.weights_input_hidden += inputs.T.dot(hidden_delta) * learning_rate
            self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

            # Print loss for every 1000 epochs
            if epoch % 1000 == 0:
                loss = np.mean(np.abs(output_errors))
                print(f"Epoch {epoch}, Loss: {loss}")

# Example usage:
if __name__ == "__main__":
    # Define the neural network architecture
    input_size = 2
    hidden_size = 3
    output_size = 1

    # Create a neural network
    neural_network = NeuralNetwork(input_size, hidden_size, output_size)

    # Training data (XOR problem)
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([[0], [1], [1], [0]])

    # Train the neural network
    neural_network.train(inputs, targets, learning_rate=0.1, epochs=10000)

    # Test the trained network
    test_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    predictions = neural_network.forward(test_input)

    print("\nPredictions:")
    print(predictions)
