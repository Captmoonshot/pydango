"""Primary function used by pydango.main"""

from pydango import (
    state
)

# from pydango.account import Account



def find_account_by_email():
    pass


def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.first_name}{state.active_account.last_name}> '
    action = input(text)
    return action.strip().lower()



def create_account():
    pass







