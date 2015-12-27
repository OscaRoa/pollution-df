from flask import Flask
from utils import WeatherData

app = Flask(__name__)


@app.route('/')
def air_pollution():
    w = WeatherData(url="http://www.aire.df.gob.mx/default.php")
    quality = w.get_air_quality()
    return "Calidad del aire: {}".format(quality)

if __name__ == '__main__':
    app.debug = True
    app.run()
