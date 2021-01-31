from pydango import (
    cinephile,
    theater_owner
)

from pydango.primary_func import (
    create_session,
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

engine, session = create_session()

def main():

    Base.metadata.create_all(engine)

    insert_category_data(session=session)
    insert_director_data(session=session)

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
















