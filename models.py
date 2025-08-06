from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base


class Password(Base):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, nullable=False)
    password = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)