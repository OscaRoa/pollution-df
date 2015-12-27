import requests


class WeatherData(object):

    def __init__(self, url="", *args, **kwargs):
        self.url = url
        super(WeatherData, self).__init__(*args, **kwargs)

    def get_air_quality(self):
        try:
            r = requests.get(self.url)
            weather = r.text.split(
                'images/iconos-recomendaciones-calidad-aire/'
                )
            quality = weather[1].split('.png')[0]
            return quality
        except:
            return "Cannot got air quality"

    def get_temp(self):
        try:
            r = requests.get(self.url)
            t = r.text.split(
                "id='calidadairetemperaturaahora'>"
                )
            temp = t[1].split('</div>')[0]
            return temp
        except:
            return "Cannot get temp."
