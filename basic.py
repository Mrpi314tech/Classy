import random
import torch
from Classy.model import NeuralNet
import nltk
from nltk.stem.porter import PorterStemmer

import requests
import urllib.parse

stemmer = PorterStemmer()


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

data=0
input_size = ''
hidden_size = ''
output_size = ''
all_words = ''
tags = ''
model_state = ''

model = 'a'
check=False
def init(location):
    global data
    global input_size
    global hidden_size
    global output_size
    global all_words
    global tags
    global model_state
    global model
    global check
    data = torch.load(location)
    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    hidden_size_2 = data["hidden_size_2"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, hidden_size_2, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()
    check=True
import numpy as np

def bag_of_words(tokenized_sentence, words):
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1
    return bag
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def classify(sentence,location):
    global check
    if check == False:
        init(location)
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)
    
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    return tag, prob.item()

def classify_api(sentence):
    sentence = urllib.parse.quote(sentence)
    response=requests.get('http://chat.mrpi314.com/api/'+sentence)
    response=response.json()
    output_tag=response['output']
    prob_int=response['certainty']
    return output_tag, float(prob_int)