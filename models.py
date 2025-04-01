from sqlalchemy import Integer, Column, VARCHAR, DateTime, Text
from datetime import datetime

from database import Base

class user(Base):
    __tablename__ = "userData"

    no = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(Text, nullable = False)
    phone = Column(Text, nullable = False)
    join_date = Column(DateTime, nullable = False, default=datetime.now)