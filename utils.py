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

    def get_time(self):
        try:
            r = requests.get(self.url)
            time = r.text.spli(
                "id='calidadairehora'>"
                )[0].split('</div>')
            return time
        except:
            return "Cannot get time."
