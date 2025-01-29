from datetime import date

from models.store import Store
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError


class StoreCrud:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_store(
        self,
        store: str,
        start_dt: date,
        state: str,
        size: int,
        industry: str,
    ):
        try:
            new_store = Store(
                store=store,
                start_dt=start_dt,
                state=state,
                size=size,
                industry=industry,
            )
            self.db.add(new_store)
            self.db.commit()
            self.db.refresh(new_store)
            return new_store
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
