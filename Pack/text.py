from . import constants
from random import choice, randint


def outstyle(text: str, style_name: str, text_start: str='', text_stop: str=''):
    return f"{text_start}\033[{constants.DATA_OUTSTYLE[style_name.replace(' ', '_')]}m{text}\033[0m\033[37m{text_stop}"


def randomstring(max_signs: int=100):
    text = ''
    for i in range(randint(1, max_signs) + 1):
        text = text + choice(constants.DATA_RANDOMTEXT)
    return text
