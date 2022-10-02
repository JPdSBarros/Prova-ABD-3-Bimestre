from sqlalchemy import create_engine, inspect

URL="mysql+mysqlconnector://localhost"

engine = create_engine(url=URL)

insp = inspect(engine)
db_list = insp.get_schema_names()


cx = engine.connect()
rs = cx.execute("SHOW DATABASES;")
for row in rs:
    print(row)
