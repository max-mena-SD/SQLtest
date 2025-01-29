from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True)
    DOB = Column(Date)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    language = Column(String)
    income = Column(Float)
    title = Column(String)
    campaign = Column(String)


class Application(Base):
    __tablename__ = "applications"
    application_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    store = Column(String, ForeignKey("stores.store"))
    submit_date = Column(Date)
    approved = Column(bool)
    approved_date = Column(Date)
    approved_amount = Column(Float)
    dollars_used = Column(Float)
    lease_grade = Column(String)


class Store(Base):
    __tablename__ = "stores"
    store = Column(String, primary_key=True)
    start_dt = Column(Date)
    state = Column(String)
    size = Column(Float)
    industry = Column(String)


class Marketing(Base):
    __tablename__ = "marketing"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    spend = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)


engine = create_engine("sqlite:///datasnap.db")

Base.metadata.create_all(engine)
