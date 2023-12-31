from app.models import User, Room, Category
import hashlib
from app import app, db
import cloudinary.uploader


def get_categories():
    return Category.query.all()


def load_rooms(page=None):
    rooms = Room.query

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size
        return rooms.slice(start, start + page_size)

    return rooms.all()


def get_room_by_id(room_id):
    return Room.query.get(room_id)


# def change_status(room_id):
#     room = Room.query.get(room_id)
#     room.active = 1 - room.active
#     return room


def count_rooms():
    return Room.query.count()


def get_booking_by_user(name=None, cccd=None):
    pass


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


def add_receipt(cart):
    if cart:
        receipt = Receipt(user=current_user)
        db.session.add(receipt)

        for c in cart.values():
            d = ReceiptDetails(quantity=c['quantity'], price=c['price'], product_id=c['id'], receipt=receipt)
            db.session.add(d)

        db.session.commit()