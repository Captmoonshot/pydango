
from sqlalchemy.orm import sessionmaker

from sqlalchemy import event

from pydango import (
    connection,
    cinephile,
    theater_owner
)
from pydango.secondary_func import (
    print_header,
    find_user_intent
)

from pydango.accounts import Account, Base


def main():
    engine = connection.create_connection()

    # Create the Account Table if it doesn't exit
    if not engine.dialect.has_table(engine, "account"):
        Base.metadata.create_all(engine)
        print(f"Creating Table: account")
        print(Account.__table__, "created\n")
    else:
        print("account table already exists!")
    
    print_header()

    try:
        while True:
            if find_user_intent() == 'find':
                cinephile.run()
            else:
                theater_owner.run()
    except KeyboardInterrupt:
        return








if __name__ == '__main__':
    main()
















