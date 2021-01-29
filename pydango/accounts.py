"""Account class for the account TABLE"""

import datetime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    Text,
)

Base = declarative_base()

class Account(Base):
    __tablename__ = "account"

    id              = Column(Integer, primary_key=True)
    email           = Column(String, nullable=False, unique=True)
    credit_card     = Column(BigInteger, nullable=False, unique=True)
    password        = Column(String, nullable=False)
    zip_code        = Column(Integer, nullable=False)
    first_name      = Column(String, nullable=True)
    last_name       = Column(String, nullable=True)
    created         = Column(DateTime, default=datetime.datetime.now)
    updated         = Column(DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return f"<self.__class__.__name__(id={self.id}, email={self.email})>"




