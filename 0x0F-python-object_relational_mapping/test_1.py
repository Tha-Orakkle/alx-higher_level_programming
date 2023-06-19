#!/usr/bin/python3
"""
Learning how to use SQLAlchemy ORM
"""

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sales.db', echo=False)
Base = declarative_base()

class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)


Base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
c1 = Customers(name = 'Ravi Kumar', address = 'Station Road Nanded', email = 'ravi@gmail.com')
session.add(c1)
session.add_all([
   Customers(name = 'Komal Pande', address = 'Koti, Hyderabad', email = 'komal@gmail.com'), 
    Customers(name = 'Rajender Nath', address = 'Sector 40, Gurgaon', email = 'nath@gmail.com'), 
   Customers(name = 'S.M.Krishna', address = 'Budhwar Peth, Pune', email = 'smk@gmail.com')]
)
session.commit()

result = session.query(Customers).all()

for row in result:
    print(row.id, "name: ", row.name, "address: ", row.address, "email: ", row.email)

x = session.query(Customers).get(2)
print("Name: ", x.name, "Address:", x.address, "Email:", x.email)
x.address = 'Banjara Hills Secunderabad'
session.commit()

cust = session.query(Customers).all()
for i in cust:
    print(i.name + " || " , end="")

session.query(Customers).filter(Customers.id != 2).update({Customers.name: "Mr. "+Customers.name}, synchronize_session=False)
session.commit()
print("\n\n============")
cust = session.query(Customers).all()
for i in cust:
    print(i.name + " || " , end="")

session.rollback()
print("\n\n============")
cust = session.query(Customers).all()
for i in cust:
    print(i.name + " || " , end="")

