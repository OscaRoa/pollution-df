from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def air_pollution():
    r = requests.get("http://www.aire.df.gob.mx/default.php")
    weather = r.text.split('images/iconos-recomendaciones-calidad-aire/')
    quality = weather[1].split('.png')[0]
    return quality

if __name__ == '__main__':
    app.debug = True
    app.run()
