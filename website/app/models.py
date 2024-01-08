from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from app import db, app
from sqlalchemy.orm import relationship
import enum
from flask_login import UserMixin



class UserRoleEnum(enum.Enum):
    USER = 1
    STAFF = 3
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(255),
                    default='https://res.cloudinary.com/dvissqsma/image/upload/v1704535651/admin_mtkbwb.jpg')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    # receipts = relationship('Receipt', backref='user', lazy=True)
    # comments = relationship('Comment', backref='user', lazy=True)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    rooms = relationship('Room', backref='category', lazy=False)

    def __str__(self):
        return self.name


class Room(db.Model):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(255), nullable=False,
                   default='https://res.cloudinary.com/dvissqsma/image/upload/v1703938812/phongdon_vlybnf.jpg')
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()

        import hashlib

        u = User(name='Admin', username='admin',
                 password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 user_role=UserRoleEnum.ADMIN)
        u1 = User(name='Quốc', username ='customer',
                 password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()))
        db.session.add(u)
        db.session.commit()

        c1 = Category(name='SingleRoom')
        c2 = Category(name='DoubleRoom')
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()

        p1 = Room(name='P001', price=210000, category_id=1)
        p2 = Room(name='P002', price=210000, category_id=2)
        p3 = Room(name='P003', price=240000, category_id=2)
        p4 = Room(name='P004', price=290000, category_id=1)
        p5 = Room(name='P101', price=250000, category_id=1)
        p6 = Room(name='P102', price=230000, category_id=1)
        p7 = Room(name='P103', price=240000, category_id=2)
        p8 = Room(name='P104', price=290000, category_id=1)
        p9 = Room(name='P201', price=250000, category_id=1)
        p10 = Room(name='P202', price=230000, category_id=1)
        p11 = Room(name='P203', price=240000, category_id=2)
        p12 = Room(name='P204', price=290000, category_id=1)
        p13 = Room(name='P301', price=250000, category_id=1)
        p14 = Room(name='P302', price=230000, category_id=1)
        db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14])
        db.session.commit()
