from flask import *
from whitenoise import WhiteNoise
app = Flask(__name__, template_folder = static)
app.wsi_app = WhiteNoise(app.wsgi_app, root='static/', prefix='static/', index_file="index.html", autorefresh=True)

@app.route('/', methods=['GET'])
def home():
  return render_template("index.html")


if __name__ == "__main__":
  app.debug = True
  app.run(threaded=True, port=5000)
