import requests


def get_air_quality(url):
    try:
        r = requests.get(url)
        weather = r.text.split('images/iconos-recomendaciones-calidad-aire/')
        quality = weather[1].split('.png')[0]
        return quality
    except:
        return "Cannot got air quality"
