import json
import numpy as np
import torch
import torch.nn as nn

from bot.nn_model import NeuralNet
from bot.dataset import ChatDataset, process_data, get_data_loader


def train():
    with open('intents.json', 'r') as f:
        intents = json.load(f)
    X_train, y_train, data = process_data(intents)
    dataset = ChatDataset(X_train, y_train)

    # Hyperparameters
    input_size = data["input_size"]
    output_size = data["output_size"]
    hidden_size = data["hidden_size"]
    batch_size = 50
    num_workers = 4
    learning_rate = 0.001
    num_epochs = 1500

    train_loader = get_data_loader(dataset, batch_size, num_workers)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = NeuralNet(input_size, hidden_size, output_size).to(device)

    # loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        for (words, labels) in train_loader:
            words = words.to(device)
            labels = labels.to(dtype=torch.long).to(device)

            # forward pass
            outputs = model(words)
            loss = criterion(outputs, labels)

            # backpropagation and optimizer
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f'epoch {epoch + 1}/{num_epochs}, loss={loss.item():.4f}')

    print(f'final loss: {loss.item():.4f}')

    data["model_state"] = model.state_dict()
    FILE = "data_test.pth"
    torch.save(data, FILE)
    print(f'training complete, file saved to "{FILE}"')


if __name__ == '__main__':
    train()
