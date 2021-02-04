# PYDANGO

pydango is a database schema that aims to mimic a movie ticket reservation database system (i.e. Fandango). It's important to note that the database represented by the package is only what I think such a system should look like, not what it actually is.

This was done in the spirit of experimentation and learning as a beginner Python programmer.

The inspiration came from a YouTube video by Mike Kennedy where he build an Air Bnb-like CLI for MongoDB with MongoEngine. I've taken a lot of his code and refactored it for SQLAlchemy and relational databases.  You can find the video here: https://youtu.be/E-1xI85Zog8

You can also find the pip-installable version of Pydango called simply "Pydango" here: https://github.com/Captmoonshot/pydango-pip that can be installed from [PyPI](https://pypi.org/project/pydango-pip/1.0.0/) with:

```pip install pydango-pip```

This regular version of Pydango is good to clone.  Once you clone it, and set up a configuration file, you can use it for both an SQLite and/or PostgreSQL database backend.

However, pydango-pip will only work with SQLite database backends.

If you're curious about the pydango database schema, you can find all the CREATE TABLE statements, along with their TRIGGER functions and the actual data used here: https://github.com/Captmoonshot/py-dango

## How to use

pydango-pip is a command line application. 

To run:

```$ python -m pydango -d sqlite```

****************** PYDANGO ******************

Welcome to Pydango for movies!
What would you like to do?

[t] List a new movie
[c] Find a movie

`# Choose [C]`

****************** Hello Cinephile ******************

What action would you like to take:
[C]reate an account
[L]ogin to your account
Log[O]ut of your account
[R]eserve a movie ticket
[V]iew your movie ticket
[S]ee list of available movies
Search for [N]earby theaters
Search by ca[T]egory
[M]ain menu
e[X]it app
[?] Help (this info)

`# Choose [S]`

****************** BROWSE FOR MOVIES ******************


Title: Pulp Fiction | Rating: R
            Description: Boxing, Robbery, Hitmen, Samuel L. Jackson

Title: Jurassic Park | Rating: PG-13
            Description: Dinosaurs, DNA, T-Rex, Velociraptor, Chaos

Title: A Clockwork Orange | Rating: R
            Description: Crazy, Crime, Future, Dystopian

Title: Aliens | Rating: R
            Description: Aliens, Eat People, Spaceship, Future

Title: Interstellar | Rating: PG-13
            Description: Apocalypse, Black Hole, Time Travel, Astronauts

--More--<ENTER>

Personally, building the project allowed me to appreciate what database engineers do for a living, and also to grokk database designs and just how complicated relational databases can get in the wild.

Special shoutout to the [Las Vegas OpenSource Programming Group](https://github.com/OpenSource-Programming/sqlforbeginners) fro challenging me to take on this project.

# To run Pydango with a PostgreSQL backend

The very first requirement is you must have PostgreSQL server installed on your machine.  Once you have that along with the proper credentials for it, go ahead and create a `config.ini` file inside of pydango the app directory: pydango/pydango/config.ini

You `config.ini` file should looke like this with your own credential information:

[postgresql]
host = localhost
database = pydango
user = postgres
password = <your_password>
port = 5432

Go into your PostgreSQL shell and create the pydango database:

```> CREATE DATBASE pydango;```

and then after that on the command line:

```$ python -m pydango```

It's important to note that if you just want to run in SQLite mode which doesn't require a database server of any type, you must provide the -d flag with sqlite:

```$ python -m pydango -d sqlite```

A good use-case is to have two Terminals running side-by-side: one terminal for the Pydango CLI, and the other hooked up to either an SQLite shell or PostgreSQL shell and try to match what's happening on the CLI with equivalent queries in the database shell.  Doing this would help a beginner programmer curious about SQL to learn things like INNER JOINs and TRIGGERs and most importantly - good database design.

For help:

`$ python -m pydango -h`

