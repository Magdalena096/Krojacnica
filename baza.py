from pony import orm
from uuid import uuid4
from datetime import datetime
import datetime as dt
import os

db =orm.Database()
db.bind(provider='sqlite',filename='baza.sqlite',create_db=True)


class Krojaci(db.Entity):
	vlasnik = orm.Required(str)
	materijal = orm.Required(str)
	kroj= orm.Required(str)
	ime = orm.Required(str)
	datum1 = orm.Required(datetime)
	datum2 = orm.Required(datetime)

class Posalji(db.Entity):
	adresa = orm.Required(str)
	broj = orm.Required(int)
	cijena = orm.Required(int)
	dostava = orm.Required(str)



db.generate_mapping(create_tables=True, check_tables=True)

