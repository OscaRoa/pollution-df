from flask import Flask
import utils

app = Flask(__name__)


@app.route('/')
def air_pollution():
    quality = utils.get_air_quality("http://www.aire.df.gob.mx/default.php")
    return "Calidad del aire: {}".format(quality)

if __name__ == '__main__':
    app.debug = True
    app.run()
