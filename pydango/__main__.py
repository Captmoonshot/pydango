#!/usr/bin/env python3

from pydango import (
    cinephile,
    theater_owner
)

from pydango.primary_func import (
    create_session,
    insert_actor_data,
    insert_category_data,
    insert_director_data,
    insert_movie_data,
    insert_theater_data,
)

from pydango.secondary_func import (
    print_header,
    find_user_intent
)

from pydango.tables import (
    Base
)

engine, session = create_session()

def main():

    Base.metadata.create_all(engine)

    # Autoload some data without user/CLI interface
    insert_category_data(session=session)
    insert_director_data(session=session)
    insert_actor_data(session=session)
    insert_movie_data(session=session)
    insert_theater_data(session=session)

    print_header()

    try:
        while True:
            if find_user_intent() == 'find':
                cinephile.run()
            else:
                theater_owner.run()
    except KeyboardInterrupt:
        return

    session.close()






if __name__ == '__main__':
    main()
















