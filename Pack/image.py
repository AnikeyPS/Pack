from requests import request


def saveimgbyurl(image_url: str, file_name: str=None):
    image = request('get', image_url)
    image_type = image_url.split('.')
    if file_name is None:
        file_name = image_type[-2].split("/")[-1]
    with open(f"{file_name}.{image_type[-1]}", 'wb') as f:
        f.write(image.content)