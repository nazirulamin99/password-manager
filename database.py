from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create SQLite database file
DATABASE_URL = "sqlite:///passwords.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()