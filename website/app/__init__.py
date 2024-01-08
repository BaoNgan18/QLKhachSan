from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = '*(^(*^897987(*^&*^&*%YUFUF&^^&$^&%&*^&*^*(^^%abhgaw4SVHD'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/quanly_khachsan?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True
app.config["PAGE_SIZE"] = 8

db = SQLAlchemy(app=app)
login = LoginManager(app=app)


import cloudinary

cloudinary.config(
    cloud_name="dvissqsma",
    api_key="943759992496484",
    api_secret="Vy5fDBMA2s0rJIgen4EMeARyTSw"
)