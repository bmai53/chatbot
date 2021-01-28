import json
import math
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from .nltk_utils import tokenize, stem, bag_of_words

class ChatDataset(Dataset):
    def __init__(self):
        X_train, y_train, _ = process_data()
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    # dataset[idx]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples


def process_data():
    with open('intents.json', 'r') as f:
        data = json.load(f)

    all_words = []
    tags = []
    xy = []  # tuple holding (x,y) pair

    for intent in data['intents']:
        tag = intent['tag']
        tags.append(tag)

        for pattern in intent['patterns']:
            w = tokenize(pattern)
            all_words.extend(w) 
            xy.append((w, tag))

    ignore_words = ['?', '!', '.', ',']
    all_words = [stem(w) for w in all_words if w not in ignore_words]
    all_words = sorted(set(all_words))

    X_train = []
    y_train = []

    for (pattern_sentence, tag) in xy:
        bag = bag_of_words(pattern_sentence, all_words)
        X_train.append(bag)

        label = tags.index(tag)
        y_train.append(label)

    X_train = np.array(X_train)
    y_train = np.array(y_train)

    data = {
        "all_words": all_words,
        "tags": tags,
        "xy":  xy,
        "input_size": len(X_train[0]),
        "output_size": len(tags),
        "hidden_size": math.floor((len(X_train[0]) + len(tags)) * 2 / 3)
    }
    return X_train, y_train, data


def get_data_loader(batch_size, num_workers):
    dataset = ChatDataset()
    train_loader = DataLoader(dataset=dataset, batch_size=batch_size, num_workers=num_workers, shuffle=True)
    return train_loader
