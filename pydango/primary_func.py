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
    Movie
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

def insert_movie_data(session):
    """Insert data for the Movie table"""
    # First check if there's existing data
    existing_movie = session.query(Movie).first()
    if existing_movie:
        return
    else:
        movies_list = [
            ('The Departed', '2006', 'R', 151, 'Irish Gangsters, Boston, Betrayal, Cops, Revenge',
            1, 1, '2020-11-1', '2021-01-01', False),
            ('Pulp Fiction', '1994', 'R', 178, 'Boxing, Robbery, Hitmen, Samuel L. Jackson',
            2, 1, '2020-12-25', '2021-12-15', True),
            ('Jurassic Park', '1993', 'PG-13', 127, 'Dinosaurs, DNA, T-Rex, Velociraptor, Chaos',
            3, 4, '2020-11-15', '2021-07-04', True),
            ('A Clockwork Orange', '1971', 'R', 136, 'Crazy, Crime, Future, Dystopian',
            4, 4, '2021-01-01', '2021-05-05', True),
            ('Aliens', '1986', 'R', 137, 'Aliens, Eat People, Spaceship, Future',
            6, 3, '2021-01-01', '2021-05-05', True),
            ('Interstellar', '2014', 'PG-13', 169, 'Apocalypse, Black Hole, Time Travel, Astronauts',
            5, 4, '2021-1-7', '2021-07-07', True),
        ]
        for i in movies_list:
            movie = Movie(
                title=i[0],
                year=i[1],
                rating=i[2],
                length_min=i[3],
                description=i[4],
                director_id=i[5],
                category_id=i[6],
                start_date=i[7],
                end_date=i[8],
                active=i[9]
            )
            session.add(movie)
            session.commit()


















