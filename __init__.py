from .New_ai import question
from . import model
from .basic import classify
from . import New_ai
from . import basic
def init(location,key):
    New_ai.init(location,key)
    basic.init(location)