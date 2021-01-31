"""Primary function used by pydango.main"""

from sqlalchemy.orm import sessionmaker
from pydango import connection

from pydango import (
    state
)

from pydango.tables import (
    Account,
    Category,
    Director,
)

def create_session():
    """Helper to create Session() object in __main__.py"""
    engine = connection.create_connection()
    Session = sessionmaker(bind=engine)
    session = Session()
    return engine, session

def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.first_name} {state.active_account.last_name}> '
    action = input(text)
    return action.strip().lower()

def insert_category_data(session):
    """Insert data for the Category table which is separate from the side that enters 
    theater data and the cinephile data"""
    # First check if there's existing data
    existing_drama = session.query(Category).first()
    if existing_drama:
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

def insert_director_data(session):
    """Insert data for the Director table"""
    # First check if there's existing data
    existing_director = session.query(Director).first()
    if existing_director:
        return
    else:
        directors_list = [
            ('Martin', 'Scorsese'),
            ('Quentin', 'Tarantino'),
            ('Steven', 'Spielberg'),
            ('Stanley', 'Kubrick'),
            ('Christopher', 'Nolan'),
            ('Scott', 'Ridley'),
        ]
        for i in directors_list:
            director = Director(first_name=i[0],
                last_name=i[1])
            session.add(director)
            session.commit()

    













