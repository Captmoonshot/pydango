"""Primary function used by pydango.main"""

from datetime import date, datetime
from dateutil.relativedelta import relativedelta

from sqlalchemy.orm import sessionmaker
from pydango import connection

from pydango import (
    state
)

from pydango.tables import (
    Account,
    Actor,
    Category,
    Director,
)

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

def insert_actor_data(session):
    """Insert data for actor Table"""
    # First check if there's existing data
    existing_actor = session.query(Actor).first()
    if existing_actor:
        return
    else:
        actors_list = [
            ('Tom', 'Hardy', '1977-09-15'),
            ('Christian', 'Bale', '1974-01-30'),
            ('Anne', 'Hathaway', '1982-11-12'),
            ('Cillian', 'Murphy', '1976-05-25'),
            ('Marion', 'Cotillard', '1975-09-30'),
            ('Joseph', 'Levitt', '1981-02-17'),
        ]

        for i in actors_list:
            actor = Actor(
                first_name=i[0],
                last_name=i[1],
                birth_day=i[2],
                # Not necessary but for precalculating age from birthday
                age=num_years(datetime.strptime(i[2], '%Y-%m-%d').date()) 
            )
            session.add(actor)
            session.commit()

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

    













