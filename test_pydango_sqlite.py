#!/usr/bin/env python3

"""tests for pydango"""



from sqlalchemy.ext.declarative import declarative_base

from pydango.tables import (
    Account,
)

Base = declarative_base()



def add_account(session, )