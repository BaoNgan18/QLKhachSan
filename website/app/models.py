from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, Boolean, DateTime
from app import app, db
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import enum
from _datetime import datetime


class UserRoleEnum(enum.Enum):
    USER = 1
    EMPLOYEE = 2
    ADMIN = 3


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100),
                    default='https://res.cloudinary.com/dvissqsma/image/upload/v1703763844/Lucciola_uk3uaw.jpg')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    # receipts = relationship('Receipt', backref='user', lazy=True)

    def __str__(self):
        return self.name


class Customer(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    address = Column(String(100), nullable=False)
    phone = Column(String(12), nullable=False)


class Room(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_name = Column(String(50), nullable=False, unique=True)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # import hashlib
        #
        # u = User(name='Admin', username='admin',
        #          password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          user_role=UserRoleEnum.ADMIN)
        # db.session.add(u)
        # db.session.commit()