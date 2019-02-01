from flask import Flask,jsonify,render_template,request
from flask_sqlalchemy import SQLAlchemy
from scrapers import getSongGenerator,songsearch

class AppConfig(object):
    AUTHOR = "Vinceeee"
    SECRET_KEY = "fxxkallindian"
    DBUSER = "tang"
    DBPASSWD = "123456"
    DEBUG = True
    DBHOST = "localhost"
    DBNAME = "test_db"
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}/{3}'.format(DBUSER, DBPASSWD, DBHOST,DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

app = Flask(__name__)
db = SQLAlchemy()
app.config.from_object(AppConfig)
db.init_app(app)

@app.route("/")
def index():
    return render_template('aplayer.html')

@app.route("/get_song")
def getSong():
    # from model import Song
    # allsong = Song.query.all()
    # song = Song.query.first()
    keywords =  request.args.get('keywords',"")

    lst = songsearch(keyword=keywords,page=1,pagesize=10)
    return jsonify([ each.toJson() for each in getSongGenerator(lst)])
    # return jsonify([ each.toJson() for each in allsong ])


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)