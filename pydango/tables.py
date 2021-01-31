"""Account class for the account TABLE"""

import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy_utils import PasswordType
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Integer,
    ForeignKey,
    ForeignKeyConstraint,
    String,
    Table,
    Text,
)

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

movie_actors = Table(
    'movie_actors',
    Base.metadata,
    Column('movie_id', ForeignKey('movie.id'), primary_key=True),
    Column('actor_id', ForeignKey('actor.id'), primary_key=True)
)

class Actor(Base):
    __tablename__ = 'actor'

    id          = Column(Integer, primary_key=True)
    first_name  = Column(String(50), nullable=True)
    last_name   = Column(String(50), nullable=True)
    birth_day   = Column(Date, nullable=True)
    age         = Column(Integer, nullable=True)
    movies      = relationship("Movie",
        secondary=movie_actors,
        back_populates="actors")

    def __repr__(self):
        return f"<{self.__class__.__name__}(first_name={self.first_name}, last_name={self.last_name})>"


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
    actors          = relationship("Actor",
            secondary=movie_actors,
            back_populates="movies")

    def __repr__(self):
        return f"<{self.__class__.__name__}(title={self.title}, year={self.year})>"

# Set the ForeignKey and relationship before creating "movie" Table
Director.movies = relationship("Movie", order_by=Movie.id, back_populates="director")
Category.movies = relationship("Movie", order_by=Movie.id, back_populates="category")


class Payment(Base):
    __tablename__ = 'payment'

    id          = Column(Integer, primary_key=True)
    credit_card = Column(BigInteger, nullable=True)
    paid        = Column(Boolean, nullable=True)

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id}, paid={self.paid})>"

    