from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime, Boolean
from sqlalchemy.orm import relationship
from app import db
from flask_login import UserMixin
import enum
from datetime import datetime


class UserRoleEnum(enum.Enum):
    USER = 1
    STAFF = 3
    ADMIN = 2


class FormTypeEnum(enum.Enum):
    BOOKING = 1
    RECEIPT = 2
    BILL = 3


class Person(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    identification = Column(String(12), unique=True, nullable=False)


class User(Person, UserMixin):
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100),
                    default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    form = relationship("BaseForm", backref="user", lazy=True)
    def __str__(self):
        return self.name


class Customer(Person):
    __tablename__ = 'customer'
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    address = Column(String(255), nullable=False)
    foreign = Column(Boolean, default=False)
    form = relationship("BaseForm", backref="room", lazy=True)
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
    maxCustomers = Column(Integer, nullable=False, default=3)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    form = relationship("Booking", backref="room", lazy=True)

    def __str__(self):
        return self.name


class BaseForm(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())
    room_id = Column(Integer, ForeignKey(Room.id), nullable=False)
    create_by = Column(Integer, ForeignKey(User.id), nullable=False)
    customer = Column(Integer, ForeignKey(Customer.id), nullable=False)


class Booking(BaseForm):
    __tablename__ = 'booking'
    typeForm = Column(Enum(FormTypeEnum), default=FormTypeEnum.BOOKING)
    expected_start_date = Column(DateTime, default=datetime.now())
    expected_end_date = Column(DateTime, default=datetime.now())

class BookingDetails(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey(Booking.id), nullable=False)
    state = Column(Boolean, default=False)
    numCustomers = Column(Integer, nullable=False, default=3)
    numRooms = Column(Integer, nullable=False, default=1)


class Receipt(BaseForm):
    __tablename__ = 'receipt'
    type = Column(Enum(FormTypeEnum), default=FormTypeEnum.RECEIPT)
    expected_start_date = Column(DateTime, default=datetime.now())
    expected_end_date = Column(DateTime, default=datetime.now())


class Bill(BaseForm):
    __tablename__ = 'bill'
    type = Column(Enum(FormTypeEnum), default=FormTypeEnum.BILL)
    end_date = Column(DateTime, default=datetime.now())
    surcharge = Column(Float, nullable=False, default=0)
    coefficient = Column(Float, nullable=False, default=0)


class Rule(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey(Room.id), nullable=False)
    surcharge = Column(Float, nullable=False, default=0)
    coefficient = Column(Float, nullable=False, default=0)


if __name__ == "__main__":
    from app import app
    with app.app_context():
        db.create_all()
        #
        # import hashlib
        # u = User(name='Admin',
        #          username='admin',
        #          password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          user_role=UserRoleEnum.ADMIN)
        # # u1 = User(name='Quốc', username ='customer',
        # #          password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()))
        # db.session.add(u)
        # db.session.commit()
        #
        # c1 = Category(name='Single')
        # c2 = Category(name='Double')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        #
        # r1 = Room(name='R001', price=240000, category_id=2,
        #              image="https://res.cloudinary.com/dvissqsma/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1703938693/phongdoi_rkhssy.jpg")
        # r2 = Room(name='R002', price=240000, category_id=2,
        #              image="https://res.cloudinary.com/dvissqsma/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1703938693/phongdoi_rkhssy.jpg")
        # r3 = Room(name='R003', price=210000, category_id=1 )
        # r4 = Room(name='R004', price=210000, category_id=1)
        # r5 = Room(name='R101', price=240000, category_id=2,
        #              image="https://res.cloudinary.com/dvissqsma/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1703938693/phongdoi_rkhssy.jpg")
        # r6 = Room(name='R102', price=230000, category_id=1)
        # r7 = Room(name='R103', price=210000, category_id=1)
        # r8 = Room(name='R104', price=240000, category_id=2,
        #              image="https://res.cloudinary.com/dvissqsma/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1703938693/phongdoi_rkhssy.jpg")
        # r9 = Room(name='R201', price=210000, category_id=1)
        # r10 = Room(name='R202', price=240000, category_id=2,
        #              image="https://res.cloudinary.com/dvissqsma/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1703938693/phongdoi_rkhssy.jpg")
        #
        # db.session.add_all([r1, r2, r3, r4, r5])
        # db.session.add_all([r6, r7, r8, r9, r10])
        # db.session.commit()
