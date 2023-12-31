from app.models import User
import hashlib
from app import app, db
import cloudinary.uploader


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()

def add_user(name, username, password, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    u = User(name=name, username=username, password=password,
             avatar='https://res.cloudinary.com/dvissqsma/image/upload/v1703763844/Lucciola_uk3uaw.jpg')

    if avatar:
        res = cloudinary.uploader.upload(avatar)
        u.avatar = res['secure_url']
    db.session.add(u)
    db.session.commit()