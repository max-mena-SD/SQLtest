from datetime import date

from models.customers import Customers
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError


class CustomerCrud:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_customer(
        self,
        customer_id: int,
        DOB: date,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        language: str,
        income: int,
        title: str,
        campaign: str,
    ):
        try:
            customer = Customers(
                customer_id=customer_id,
                DOB=DOB,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                language=language,
                income=income,
                title=title,
                campaign=campaign,
            )
            # self.db.add(customer)
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except IntegrityError as e:
            self.db.rollback()
            print(f"Integrity error: {e}", end="\r", flush=True)
            return None
        except OperationalError as e:
            self.db.rollback()
            print(f"Operational error: {e}", end="\r", flush=True)
            return None
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"An unexpected error occurred: {e}", end="\r", flush=True)
            return None
