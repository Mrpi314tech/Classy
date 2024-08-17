from .functions import personal
from .functions import chat_gpt
from .functions import dall_e
from .functions import search





from .server import server
from . import model
from .basic import classify
from .basic import classify_api
from . import server
from . import basic
import time
import os
import nltk
def init(location,key,user_name):
    New_ai.init(location,key,user_name)
def download():
    print('Downloading the model from GitHub. Press Ctrl+c to quit.')
    time.sleep(3)
    os.system('wget https://github.com/Mrpi314tech/Classy/raw/main/train/data.pth')
    print('Downloading nltk tokenizer. Press Ctrl+c to quit.')
    time.sleep(3)
    nltk.download('punkt')