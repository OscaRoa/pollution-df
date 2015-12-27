from flask import Flask, jsonify
from utils import WeatherData

app = Flask(__name__)


@app.route('/')
def air_pollution():
    w = WeatherData(url="http://www.aire.df.gob.mx/default.php")
    quality = w.get_air_quality()
    temp = w.get_temp()
    return jsonify(air_quality=quality,
                   current_temp=temp)

if __name__ == '__main__':
    app.debug = True
    app.run()
