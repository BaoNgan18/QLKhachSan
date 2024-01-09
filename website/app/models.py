import hashlib

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime, Boolean
from sqlalchemy.orm import relationship
from app import db
from flask_login import UserMixin
import enum
from datetime import datetime


class UserRoleEnum(enum.Enum):
    USER = 1
    CUSTOMER = 3
    ADMIN = 2


class Person(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    identification = Column(String(12), unique=True, nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)


class User(Person, UserMixin):

    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    phone = Column(String(12), nullable=True)
    # form = relationship("BaseForm", backref="user", lazy=True)
    def __str__(self):
        return self.name


class Customer(Person):
    __tablename__ = 'customer'
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.CUSTOMER)
    address = Column(String(255), nullable=False)
    foreign = Column(Boolean, default=False)   #khach nuoc ngoai
    # booking = relationship("Booking", backref="customer", lazy=True)
    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    Rooms = relationship('Room', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Room(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    image = Column(String(255), default="https://res.cloudinary.com/dvissqsma/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1703938812/phongdon_vlybnf.jpg")
    status = Column(String(255), nullable=True)
    maxCustomers = Column(Integer, nullable=False, default=2)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    # booking = relationship("Booking", secondary="booking_details", backref="room", lazy=True)
    # receipt = relationship("Receipt", backref="room", lazy=True)
    def __str__(self):
        return self.name

#
# class BaseForm(db.Model):
#     __abstract__ = True
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     created_date = Column(DateTime, default=datetime.now()) #ngay dat phong
#     user_id = Column(Integer, ForeignKey(User.id), nullable=False)
#     customer = Column(Integer, ForeignKey(Customer.id), nullable=False)
#
#
# class Booking(BaseForm):
#     __tablename__ = 'booking'
#     start_date = Column(DateTime, default=datetime.now()) #ngay nhan phong du kien
#     expected_end_date = Column(DateTime, default=datetime.now())    #ngay tra phong du kien
#     booking_details = relationship("BookingDetails", backref="booking", lazy=True)
#
#
# BookingDetails = db.Table('booking_details',
#     Column("booking_id",Integer, ForeignKey(Booking.id), nullable=False),
#     Column("room_id", Integer, ForeignKey(Room.id), nullable=False),
#     Column("status", Boolean, default=False), #nhan || chua nhan phong
#     Column("numCustomers", Integer, nullable=False, default=1),
#     Column("numRooms", Integer, nullable=False, default=1)),
#
#
# class Receipt(BaseForm):
#     __tablename__ = 'receipt'
#     expected_end_date = Column(DateTime, default=datetime.now())  # ngay tra phong du kien
#
#
# class Bill(BaseForm):
#     __tablename__ = 'bill'
#     total = Column(Float, nullable=False, default=0)
#     surcharge = Column(Float, nullable=False, default=0)    #phu thu
#     coefficient = Column(Float, nullable=False, default=1)  #he so
#
#
# class Rule(db.Model):
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     room_id = Column(Integer, ForeignKey(Room.id), nullable=False)
#     surcharge = Column(Float, nullable=False, default=0)
#     coefficient = Column(Float, nullable=False, default=0)


if __name__ == "__main__":
    from app import app
    with app.app_context():
        db.create_all()

        # import hashlib
        # u = User(name='Admin',
        #          username='admin',
        #          identification='0123123123',
        #          password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          user_role=UserRoleEnum.ADMIN)

        # u1 = User(name='customer', username ='Quốc', identification='987654321123',
        #          password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()))
        # db.session.add_all([u1])
        # db.session.commit()

        # c1 = Category(name='Single', description='phong co 1 giuong ngu', price='120000')
        # c2 = Category(name='Double', description='phong co 2 giuong ngu', price='150000')
        #
        # db.session.add(c1, c2)
        # db.session.add(c2)
        # db.session.commit()
        #
        # r1 = Room(name='R001', category_id=2, status="san sang",
        #              image="https://res.cloudinary.com/dvissqsma/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1703938693/phongdoi_rkhssy.jpg")
        # r2 = Room(name='R002',  status="san sang", category_id=2,
        #              image="https://res.cloudinary.com/dvissqsma/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1703938693/phongdoi_rkhssy.jpg")
        # r3 = Room(name='R003',  status="san sang", category_id=1 )
        # r4 = Room(name='R004',  status="san sang", category_id=1)
        # r5 = Room(name='R101',  status="san sang", category_id=2,
        #              image="https://res.cloudinary.com/dvissqsma/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1703938693/phongdoi_rkhssy.jpg")
        # r6 = Room(name='R102', status="san sang", category_id=1)
        # r7 = Room(name='R103',  status="san sang", category_id=1)
        # r8 = Room(name='R104',  status="san sang", category_id=2,
        #              image="https://res.cloudinary.com/dvissqsma/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1703938693/phongdoi_rkhssy.jpg")
        # r9 = Room(name='R201',  status="san sang", category_id=1)
        # r10 = Room(name='R202',  status="san sang", category_id=2,
        #              image="https://res.cloudinary.com/dvissqsma/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1703938693/phongdoi_rkhssy.jpg")
        #
        # db.session.add_all([r1, r2, r3, r4, r5])
        # db.session.add_all([r6, r7, r8, r9, r10])
        # db.session.commit()
