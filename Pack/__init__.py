# Utils-pack 1.0
from requests import request
from . import constants


def saveimgbyurl(image_url: str, file_name: str):
    image = request('get', image_url)
    image_type = image_url.split('.')[-1]
    with open(f"{file_name}.{image_type}", 'wb') as f:
        f.write(image.content)


def outstyle(text: str, style_name: str, text_start: str='', text_stop: str=''):
    return f"{text_start}\033[{DATA_OUTSTYLE[style_name.replace(' ', '_')]}m{text}\033[0m\033[37m{text_stop}"
