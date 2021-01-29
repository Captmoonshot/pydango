from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

from pydango import state
from pydango.switchlang import switch
from pydango import connection

from pydango import (
    primary_func,
    secondary_func
)

from pydango.accounts import Account


def run():
    print('****************** Hello Cinephile ******************')
    print()
    
    show_commands()

    while True:
        action = primary_func.get_action()

        with switch(action) as s:
            s.case('c', create_account)
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
    print('[R]eserve a movie ticket')
    print('[V]iew your movie ticket')
    print('[S]ee list of available movies')
    print('[M]ain menu')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()

def create_account():
    engine = connection.create_connection()
    Session = sessionmaker(bind=engine)
    session = Session()

    print("****************** REGISTER ******************")

    print()
    print("Please provide the following information\n")

    email = input("Email (required): ").strip().lower()
    credit_card = input("Credit-card number (required, i.e. 4444333399993333): ")
    credit_card = int(credit_card)
    password = input("Password (required): ")
    zip_code = input("Zip-code (required): ")
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
        last_name=last_name
    )
    session.add(account)

    my_account = session.query(Account).filter_by(email=email).first()

    session.commit()

    state.active_account = account
    secondary_func.success_msg(f"\nCreated new account with id {state.active_account.id}")

    session.close()






















