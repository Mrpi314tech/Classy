import torch
import torch.nn as nn
# Set up nn, 1 hidden layer
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        # Define the single hidden layer
        self.l1 = nn.Linear(input_size, hidden_size) 
        # Define the output layer
        self.l2 = nn.Linear(hidden_size, num_classes)
        # Activation function
        self.relu = nn.ReLU()
    
    def forward(self, x):
        # Apply first linear layer
        out = self.l1(x)
        # Apply ReLU activation
        out = self.relu(out)
        # Apply second linear layer
        out = self.l2(out)
        # No activation or softmax at the end
        return out
