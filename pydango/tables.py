"""Account class for the account TABLE"""

import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy_utils import PasswordType
from sqlalchemy import (
    event,
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Integer,
    ForeignKey,
    String,
    Text,
)
from sqlalchemy.orm import sessionmaker

from pydango import connection

def yearsago(years, from_date=None):
    """Helper function for calculating the date n years ago
    To be used for receive_before_actor_attach function
    To calculate age of actor"""
    if from_date is None:
        from_date = date.today()
    return from_date - relativedelta(years=years)

def num_years(begin, end=None):
    """Helper function for calculating the date n years ago
    To be used for receive_before_actor_attach function
    To calculate age of actor"""
    if end is None:
        end = date.today()
    num_years = int((end - begin).days / 365.25)
    if begin > yearsago(num_years, end):
        return num_years - 1
    else:
        return num_years

def get_session_obj():
    """Helper function to generation Session obj"""
    engine = connection.create_connection()
    Session = sessionmaker(bind=engine)
    return Session


Base = declarative_base()

class Account(Base):
    __tablename__ = "account"

    id              = Column(Integer, primary_key=True)
    email           = Column(String(50), nullable=False, unique=True)
    credit_card     = Column(BigInteger, nullable=False)
    # sqlalchemy_utils.PasswordType requires passlib
    # pip install passlib
    password        = Column(PasswordType(
                schemes=[
                    'pbkdf2_sha512',
                    'md5_crypt'
                ],
                deprecated=['md5_crypt']
    ), unique=False, nullable=False)
    zip_code        = Column(Integer, nullable=False)
    first_name      = Column(String(30), nullable=True)
    last_name       = Column(String(30), nullable=True)
    theater_owner   = Column(Boolean, nullable=True)
    created         = Column(DateTime, default=datetime.datetime.now)
    updated         = Column(DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id}, email={self.email})>"

class Actor(Base):
    __tablename__ = 'actor'

    id          = Column(Integer, primary_key=True)
    first_name  = Column(String(50), nullable=True)
    last_name   = Column(String(50), nullable=True)
    birth_day   = Column(Date, nullable=True)
    age         = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<{self.__class__.__name__}(first_name={self.first_name}, last_name={self.last_name})>"
    
# @event.listens_for(Session, 'before_attach')
# def receive_before_actor_attach(session, instance):
#     "listens for the 'before_attach' event"
#     age = num_years(begin=instance.birth_day, end=None)
#     instance.age = age

class Category(Base):
    __tablename__ = "category"

    id              = Column(Integer, primary_key=True)
    category_name   = Column(String(50), unique=True, nullable=True)

    def __repr__(self):
        return f"<{self.__class__.__name__}(name={self.category_name})>"


class Director(Base):
    __tablename__ = 'director'

    id          = Column(Integer, primary_key=True)
    first_name  = Column(String(50), nullable=True)
    last_name   = Column(String(50), nullable=True)

    def __repr__(self):
        return f"<{self.__class__.__name__}(first_name={self.first_name}, last_name={self.last_name})>"


class Movie(Base):
    __tablename__ = 'movie'

    id              = Column(Integer, primary_key=True)
    title           = Column(String(50), nullable=False)
    year            = Column(Integer, nullable=True)
    rating          = Column(String(5), nullable=True)
    length_min      = Column(Integer, nullable=True)
    description     = Column(Text, nullable=True)
    director_id     = Column(Integer, ForeignKey(
            'director.id',
            ondelete='CASCADE'
    ))
    director        = relationship("Director", back_populates='movies')
    category_id     = Column(Integer, ForeignKey(
            'category.id',
            ondelete='CASCADE'
    ))
    category        = relationship("Category", back_populates='movies')
    start_date      = Column(Date, nullable=True)
    end_date        = Column(Date, nullable=True)
    active          = Column(Boolean, nullable=True)

    def __repr__(self):
        return f"<{self.__class__.__name__}(title={self.title}, year={self.year})>"

# Set the ForeignKey and relationship before creating "movie" Table
Category.movies = relationship("Movie", order_by=Movie.id, back_populates="category")
Director.movies = relationship("Movie", order_by=Movie.id, back_populates="director")




class Payment(Base):
    __tablename__ = 'payment'

    id          = Column(Integer, primary_key=True)
    credit_card = Column(BigInteger, nullable=True)
    paid        = Column(Boolean, nullable=True)

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id}, paid={self.paid})>"

    