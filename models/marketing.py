from sqlalchemy import Column, Integer, String, Float, Date
from .base import Base


class Marketing(Base):
    __tablename__ = "marketing"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    spend = Column(Float)  # Assuming marketing spend could have decimals
    start_date = Column(Date)
    end_date = Column(Date)
