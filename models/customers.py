from sqlalchemy import Column, String, Integer, Date
from .base import Base


class Customers(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)
    DOB = Column(Date)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    language = Column(String)
    income = Column(Integer)  # Assuming annual income is a whole number
    title = Column(String)
    campaign = Column(String)


# customer_id	A unique identifier assigned to each customer
# DOB	Date of Birth of the customer
# first_name	First name of the customer
# last_name	Last name of the customer
# email	Email address of the customer
# phone_number	Phone number of the customer
# language	Preferred language of the customer
# income	Annual income of the customer
# title	Job title of the customer
# campaign	Campaign through which the customer was acquired or contacted
