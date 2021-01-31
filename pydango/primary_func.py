"""Primary function used by pydango.main"""

from pydango import (
    state
)

from sqlalchemy.orm import sessionmaker

from pydango import connection

from pydango.tables import Account
from pydango.tables import Category



def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.first_name} {state.active_account.last_name}> '
    action = input(text)
    return action.strip().lower()

def insert_category_data(session):
    """Create the Category table which is separate from the side that enters theater data
    and the cinephile data"""
    # First check if there's existing data
    drama = session.query(Category).filter_by(category_name='Drama').first()
    if drama:
        return
    else:
        categories_list = [
            'Drama',
            'Action',
            'Horror',
            'Scifi',
            'Romance',
            'Comedy',
        ]
        for cat in categories_list:
            category = Category(category_name=cat)
            session.add(category)
            session.commit()
    











