# Utils-pack 1.3
from requests import request
from . import constants
from random import choice, randint


def saveimgbyurl(image_url: str, file_name: str=None):
    image = request('get', image_url)
    image_type = image_url.split('.')
    if file_name is None:
        file_name = image_type[-2].split("/")[-1]
    with open(f"{file_name}.{image_type[-1]}", 'wb') as f:
        f.write(image.content)


def outstyle(text: str, style_name: str, text_start: str='', text_stop: str=''):
    return f"{text_start}\033[{constants.DATA_OUTSTYLE[style_name.replace(' ', '_')]}m{text}\033[0m\033[37m{text_stop}"


def randomstring(max_signs: int=100):
    text = ''
    for i in range(randint(1, max_signs) + 1):
        text = text + choice(constants.DATA_RANDOMTEXT)
    return text
