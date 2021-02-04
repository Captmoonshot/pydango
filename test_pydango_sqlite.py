#!/usr/bin/env python3

"""tests for pydango"""


import sqlite3


from pydango.tables import (
    Account,
)
from pydango.primary_func import (
    insert_account_data,
)


def test_add_account(db_session):
    """Add data to account table"""
    # Note: if you add more data to pydango.init_data.accounts_list
    # this test will fail
    insert_account_data(session=db_session)
    test_accounts = db_session.query(Account).all()
    alex = test_accounts[0]
    assert len(test_accounts) == 3
    assert alex.email == 'alex@gmail.com'
    




    
