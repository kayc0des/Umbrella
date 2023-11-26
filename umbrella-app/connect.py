from sqlalchemy import create_engine, text


# Engine Object - takes at least one positional argument which is the path to the database
engine = create_engine("mysql+mysqlconnector://root:kayc0des@localhost/umbrella", echo=True)

#test connection
with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))

    print(result.all())