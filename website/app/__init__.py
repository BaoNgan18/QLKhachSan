from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = '*(^(*^897987(*^&*^&*%YUFUF&^^&$^&%&*^&*^*(^^%abhgaw4SVHD'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/hotel?charset=utf8mb4" % quote('Jerz813@')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 2

db = SQLAlchemy(app=app)
# login = LoginManager(app=app)


import cloudinary

cloudinary.config(
    cloud_name="dvissqsma",
    api_key="943759992496484",
    api_secret="Vy5fDBMA2s0rJIgen4EMeARyTSw"
)