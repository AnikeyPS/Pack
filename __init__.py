from requests import request


def saveimgbyurl(image_url: str, file_name: str):
    image = request('get', image_url)
    image_type = image_url.split('.')[-1]
    with open(f"{file_name}.{image_type}", 'wb') as f:
        f.write(image.content)


def outstyle(text: str, style_id: int, text_start: str='', text_stop: str=''):
    return f"{text_start}\033[{str(style_id)}m{text}\033[0m\033[37m{text_stop}"
