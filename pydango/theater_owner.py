from datetime import date, datetime
from getpass import getpass

from pydango import state
from pydango.switchlang import switch

from pydango import (
    primary_func,
    secondary_func
)

from pydango.primary_func import (
    create_session,
    yearsago,
    num_years
)

from pydango.tables import (
    Account,
    Actor,
    Category,
    Director,
    Movie
)

from pydango.cinephile import log_into_account

engine, session = create_session()

def run():
    print('****************** Hello Theater Owner ******************')
    print()
    
    show_commands()

    while True:
        action = primary_func.get_action()

        with switch(action) as s:
            s.case('c', create_account)
            s.case('l', log_into_account)
            s.case('p', create_movie)
            s.case('a', create_actor)
            s.case('m', lambda: 'change_mode')
            s.case(['x', 'bye', 'exit', 'exit()'], secondary_func.exit_app)

            s.default(secondary_func.unknown_command)

        
        if action:
            print()

        if s.result == 'change_mode':
            return



def show_commands():
    print('What action would you like to take: ')
    print('[C]reate an account')
    print('[L]ogin to your account')
    print('[P]ost a Movie')
    print('Enter [A]ctor Information')
    print('[M]ain menu')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()

def create_account():
    """Violation of DRY principle"""

    print("****************** REGISTER ******************")

    print()
    print("Please provide the following information\n")

    email = input("Email (required): ").strip().lower()
    credit_card = input("Credit-card number (required, i.e. 4444333399993333): ").strip()
    credit_card = int(credit_card)
    password = getpass().strip()
    zip_code = input("Zip-code (required): ").strip()
    zip_code = int(zip_code)
    first_name = input("What is your first name? ").strip()
    last_name = input("What is your last name? ").strip()

    old_account = session.query(Account).filter_by(email=email).first()
    if old_account:
        secondary_func.error_msg(f"ERROR: Account with email {email} already exists.")
        return

    account = Account(
        email=email,
        credit_card=credit_card,
        password=password,
        zip_code=zip_code,
        first_name=first_name,
        last_name=last_name,
        theater_owner=True
    )
    session.add(account)

    # Flush
    my_account = session.query(Account).filter_by(email=email).first()

    session.commit()

    state.active_account = account
    secondary_func.success_msg(f"\nCreated new account with id {state.active_account.id}")


def create_actor():
    print("****************** POST AN ACTOR ******************")
    print()

    if not state.active_account:
        secondary_func.error_msg("You must be logged in to post a movie.")
        return
    if not state.active_account.theater_owner == True:
        secondary_func.error_msg("You must be a theater owner to post a new movie.")
        return
    
    print("Provide the following information\n")

    first_name = input("Actor's first name: ").strip()
    last_name = input("Actor's last name: ").strip()
    birth_day = input("Actor's birthday (YYYY-MM-DD): ").strip()
    birth_day = datetime.strptime(birth_day, '%Y-%m-%d').date()
    # calculate age from birth_day using num_years()
    age = num_years(birth_day)

    actor = Actor(
        first_name=first_name,
        last_name=last_name,
        birth_day=birth_day,
        age=age
    )

    session.add(actor)
    session.commit()

    print("\nSuccess!\n")

def create_movie():
    print("****************** POST A NEW MOVIE ******************")
    print()

    if not state.active_account:
        secondary_func.error_msg("You must be logged in to post a movie.")
        return
    if not state.active_account.theater_owner == True:
        secondary_func.error_msg("You must be a theater owner to post a new movie.")
        return

    # prep actor data
    actors = session.query(Actor).all()

    print("Provide the following information\n")

    title = input("Title: ").strip()
    year = input("Year: ").strip()
    year = int(year)
    rating = input("Rating: ").strip()
    length_min = input("Length of movie in minutes: ").strip()
    length_min = int(length_min)
    description = input("""Movie description: """)
    director_first_name = input("Director's first name: ").strip()
    director_last_name = input("Director's last name: ").strip()
    category_name = input("Movie category: (i.e. Drama)  ").strip()
    start_date = input("Enter the start date: (YYYY-MM-DD) ").strip()
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = input("Enter the end date: (YYYY-MM-DD) ").strip()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    
    # List all available actors:
    if actors:
        print("\nList of available actors:\n")
        for actor in actors:
            print(actor.first_name, actor.last_name, actor.age)
            print()

    # For Many-To-Many relationship between movies and actors
    main_first_name = input("Enter main actor's first name: ").strip()
    main_last_name = input("Enter main actor's last name: ").strip()
    another_actor = input("Do you wish to enter another actor (Yes or No)? ")
    if another_actor == "Yes" or another_actor == "Y" or another_actor == "yes" or another_actor == "y":
        supporting_first_name = input("Enter supporting actor's first name: ").strip()
        supporting_last_name = input("Enter supporting actor's last name: ").strip()
    else:
        supporting_first_name = None
        supporting_last_name = None   

    def get_active():
        # Emulating an SQL trigger function
        today = date.today()
        if start_date <= today <= end_date:
            return True
        return False

    if supporting_first_name is not None and supporting_last_name is not None:
        supporting_actor = session.query(Actor).filter_by(
            first_name=supporting_first_name,
            last_name=supporting_last_name
        ).first()
    else:
        supporting_actor = None

    main_actor = session.query(Actor).filter_by(
        first_name=main_first_name,
        last_name=main_last_name
    ).first()
        

    # Grab the relevant ids for the ForeignKey relationship
    director = session.query(Director).filter_by(
        first_name=director_first_name,
        last_name=director_last_name
    ).first()

    # Grab the relevant ids for the ForeignKey relationship
    category = session.query(Category).filter_by(
        category_name=category_name
    ).first()

    movie = Movie(
        title=title,
        year=year,
        rating=rating,
        length_min=length_min,
        description=description,
        director_id=director.id,
        category_id=category.id,
        start_date=start_date,
        end_date=end_date,
        active=get_active()
    )
    movie.actors.append(main_actor)
    if supporting_actor is not None:
        movie.actors.append(supporting_actor)

    session.add(movie)

    session.commit()

    print("\nSucess!\n")








    










