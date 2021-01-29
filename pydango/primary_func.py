"""Primary function used by pydango.main"""

from pydango import (
    state
)

from sqlalchemy.orm import sessionmaker

from pydango import connection

from pydango.accounts import Account



def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.first_name} {state.active_account.last_name}> '
    action = input(text)
    return action.strip().lower()








