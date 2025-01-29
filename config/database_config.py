from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from repositories.base_repository import BaseRepository


# Database connection URL
class DatabaseConfig:
    def __init__(self, DATABASE_URL):
        self.DATABASE_URL = DATABASE_URL

    def get_session(self):
        # Create the engine
        engine = create_engine(self.DATABASE_URL)

        # Create the session
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        session = SessionLocal()

        # Initialize the BaseRepository with a session
        repository = BaseRepository(session)

        # Create all tables
        Base.metadata.create_all(bind=engine)

        return session
