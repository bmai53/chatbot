import random
import json
import os
import torch
from .nn_model import NeuralNet
from .nltk_utils import bag_of_words, tokenize


class ChatBot():

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def __init__(self):
        with open('responses.json', 'r') as f:
            self.responses = json.load(f)

        FILE = 'data.pth'
        data = torch.load(os.path.join(os.path.dirname(__file__), '..', FILE))

        self.input_size = data["input_size"]
        self.hidden_size = data["hidden_size"]
        self.output_size = data["output_size"]

        self.all_words = data["all_words"]
        self.tags = data["tags"]
        self.model_state = data["model_state"]

        self.model = NeuralNet(
            self.input_size, self.hidden_size, self.output_size).to(ChatBot.device)
        self.model.load_state_dict(self.model_state)  # load learned parameters
        self.model.eval()

    def chat(self, sentence):
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, self.all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(ChatBot.device)

        # get result from model
        output = self.model(X)
        _, predicted = torch.max(output, dim=1)
        tag = self.tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:
            for response_data in self.responses["response_data"]:
                if tag == response_data["tag"]:
                    return random.choice(response_data['responses'])
        else:
            return "I do not understand ):"
