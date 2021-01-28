import torch
import torch.nn as nn


class NeuralNet(nn.Module):

    def __init__(self, input_size, hidden_size, num_classes):
        """
        NeuralNet.__init__():

        input_size:     number of patterns (inputs)
        hidden_size:    number of nodes in hidden layer
        num_classes:    number of tags (outputs)
        """
        super().__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()  # activation function

    def forward(self, x):
        """
        NeuralNet.forward():

        - uses nn.Linear():
            layer = nn.Linear(input_size, output_size)
            output = layer(input)
        """
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # no activation and no softmax at end
        return out
