"""Notes to help complete the project"""
from pydango.primary_func import create_session

engine, session = create_session()

from pydango.tables import (
    Account,
    Payment,
    Theater,
    Movie,
    Ticket,
    theater_schedule,
)

account = session.query(Account).filter_by(first_name='Sammy', last_name='Lee').first()

print(account.id)
print(account.credit_card)

schedules = session.query(theater_schedule).all()

# Show movie theater schedule to user:
index = 0
for i in schedules:
    theater = session.query(Theater).filter_by(id=i.theater_id).first()
    movie = session.query(Movie).filter_by(id=i.movie_id).first()
    index += 1
    print(f"""{index}: {theater.name} {theater.address}, Prices: {theater.ticket_price}
    {movie.title}, Schedules: {i.time}, Seats: {i.seats_available}""")
    print()

# Put the choices for movie theaters schedule into a list they can choose from 
theaters_list = []
payment_id = 0
for i, x in enumerate(schedules, 1):
    theater = session.query(Theater).filter_by(id=x.theater_id).first()
    movie = session.query(Movie).filter_by(id=x.movie_id).first()
    payment_id += 1
    quantity = 1
    category = 'Adult'
    total = theater.ticket_price[category] * quantity
    total = float(total)
    tup = (i, theater.id, movie.id, x.time, payment_id, account.id, quantity, total)
    theaters_list.append(tup)

# Users will supply values for quantity and whether they're paying Adult/Child tickets

print(theaters_list)

ticket_number = input("Enter ticket number: ").strip()
ticket_number = int(ticket_number) - 1

my_ticket = theaters_list[ticket_number]

ticket = Ticket(
    theater_id=my_ticket[1],
    movie_id=my_ticket[2],
    time=my_ticket[3],
    payment_id=my_ticket[4],
    account_id=my_ticket[5],
    quantity=my_ticket[6],
    total=my_ticket[7]
)

payment = Payment(
    id=ticket.payment_id,
    credit_card=account.credit_card,
    paid=True
)

session.add(ticket)
session.add(payment)

session.commit()




