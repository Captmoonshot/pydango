from pydango import (
    connection,
    cinephile,
    theater_owner
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

    Base.metadata.create_all(engine)

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
















