from datetime import date

from models.marketing import Marketing
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError


class MarketingCrud:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_marketing_campaign(
        self,
        id: int,
        name: str,
        spend: float,
        start_date: date,
        end_date: date,
    ):
        try:
            campaign = Marketing(
                id=id,
                name=name,
                spend=spend,
                start_date=start_date,
                end_date=end_date,
            )
            self.db.add(campaign)
            self.db.commit()
            self.db.refresh(campaign)
            return campaign
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
