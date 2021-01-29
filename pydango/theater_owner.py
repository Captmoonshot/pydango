from pydango.switchlang import switch

from pydango import (
    primary_func,
    secondary_func
)


def run():
    print('****************** Hello Cinephile ******************')
    print()
    
    show_commands()

    while True:
        action = primary_func.get_action()

        with switch(action) as s:
            s.case('c', create_account)
            s.case('m', lambda: 'change_mode')

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
    pass




