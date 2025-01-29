from datetime import date
from sqlite3 import IntegrityError
from models.applications import Applications
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError


class ApplicationCrud:

    def __init__(self, db: Session) -> None:
        self.db = db

    def create_application(
        self,
        application_id: str,
        customer_id: int,
        store: str,
        submit_date: date,
        approved: bool,
        approved_date: date,
        approved_amount: float,
        dollars_used: float,
        lease_grade: str,
    ):
        try:
            app = Applications(
                application_id=application_id,
                customer_id=customer_id,
                store=store,
                submit_date=submit_date,
                approved=approved,
                approved_date=approved_date,
                approved_amount=approved_amount,
                dollars_used=dollars_used,
                lease_grade=lease_grade,
            )
            self.db.add(app)
            self.db.commit()
            self.db.refresh(app)
            return app
        except IntegrityError as e:
            self.db.rollback()
            print(
                f"Integrity error: {e}", end="\r", flush=True
            )  # Handle constraint violations
            return None
        except OperationalError as e:
            self.db.rollback()
            print(
                f"Operational error: {e}", end="\r", flush=True
            )  # Handle database errors
            return None
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"An unexpected error occurred: {e}", end="\r", flush=True)
            return None
