from .New_ai import question
from . import model
from .basic import classify
from . import New_ai
from . import basic
import time
import os
import nltk
def init(location,key):
    New_ai.init(location,key)
    basic.init(location)
def download():
    print('Downloading the model from GitHub. Press Ctrl+c to quit.')
    time.sleep(3)
    os.system('wget https://github.com/Mrpi314tech/Classy/raw/main/train/data.pth')
    print('Downloading nltk tokenizer. Press Ctrl+c to quit.')
    time.sleep(3)
    nltk.download('punkt')