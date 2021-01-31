
from sqlalchemy.orm import sessionmaker

from pydango import (
    connection,
    cinephile,
    theater_owner
)

from pydango.primary_func import (
    insert_category_data,
    insert_director_data,
)

from pydango.secondary_func import (
    print_header,
    find_user_intent
)

from pydango.tables import (
    Base
)

def main():

    engine = connection.create_connection()
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    insert_category_data(session=session)
    insert_director_data(session=session)
    
    session.close()

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
















