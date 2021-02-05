import random
import json
import os
from better_profanity import profanity
import torch
from .nn_model import NeuralNet
from .nltk_utils import bag_of_words, tokenize


class ChatBot():

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def __init__(self):
        profanity.load_censor_words()

        with open('responses.json', 'r') as f:
            self.responses = json.load(f)

        FILE = os.path.join(os.path.dirname(__file__), '..', 'data.pth')
        # if no cuda
        map_location = None if torch.cuda.is_available() else 'cpu'
        data = torch.load(FILE, map_location=map_location)

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

    def bad_sentence(self):
        for response_data in self.responses["response_data"]:
            if response_data["tag"] == "bad":
                return {
                    "msg": random.choice(response_data["responses"]),
                    "tag": "bad",
                    "profanity": True
                }

    def no_intent_detected(self):
        return {
            "tag": None,
            "msg": random.choice([
                "Sorry, I don't understand :(",
                "I'm sorry, could you rephrase that?",
                "Sorry, I'm having troubles understanding you",
                "Sorry, that doesn't make sense to me :(",
                "I'm sorry, I dont quite understand"
            ])
        }

    def make_response(self, tag):
        for response_data in self.responses["response_data"]:
            if tag == response_data["tag"]:

                bot_response = {
                    "msg": random.choice(response_data["responses"]),
                    "tag": tag
                }

                if "link" in response_data:
                    bot_response["link"] = response_data["link"]
                    return bot_response

                return bot_response

    def chat(self, sentence):

        if(profanity.contains_profanity(sentence)):
            return self.bad_sentence()

        sentence = tokenize(sentence)
        X = bag_of_words(sentence, self.all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(ChatBot.device)

        # get result from model
        output = self.model(X)
        all, predicted = torch.max(output, dim=1)
        tag = self.tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        print(
            f'\n\ChatBot Prediction: \n\tsentence: {sentence} \n\tpredicted: {tag} \n\tprobability: {prob}\n')

        if prob.item() > 0.75:
            return self.make_response(tag)
        else:
            return self.no_intent_detected()
