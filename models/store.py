from sqlalchemy import Column, String, Date, Integer
from .base import Base


class Store(Base):
    __tablename__ = "stores"

    store = Column(String, primary_key=True)
    start_dt = Column(Date)
    state = Column(String)
    size = Column(Integer)  # Assuming revenue size is a whole number
    industry = Column(String)
