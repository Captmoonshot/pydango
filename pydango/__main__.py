from importlib import resources

from sqlalchemy.orm import sessionmaker
from sqlalchemy import event


from pydango import connection

def main():
    engine = connection.create_connection()
    Session = sessionmaker(bind=engine)

    print(engine)
    print(Session)


if __name__ == '__main__':
    main()
















