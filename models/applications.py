from sqlalchemy import Column, String, Integer, Date, Boolean, Float, ForeignKey
from .base import Base


class Applications(Base):
    __tablename__ = "applications"

    application_id = Column(String, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    store = Column(String, ForeignKey("stores.store"))
    submit_date = Column(Date)
    approved = Column(Boolean)
    approved_date = Column(Date)
    approved_amount = Column(Float)
    dollars_used = Column(Float)
    lease_grade = Column(String)


# applications
# application_id	A unique identifier assigned to each application
# customer_id	A unique identifier assigned to each customer who applied (Foreign Key to Customer Table)
# store	The store location where the application was submitted (Foreign Key to Store Table)
# submit_date	The date when the application was submitted
# approved	A flag indicating whether the application was approved or not
# approved_date	The date when the application was approved
# approved_amount	The amount approved
# dollars_used	The dollar amount used by the customer
# lease_grade	the grade of the lease
