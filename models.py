from sqlalchemy import Column, Integer, String, Text
from database import Base

class Dataset(Base):
    __tablename__ = "datasets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=True)
    file_type = Column(String(20), nullable=False)
    records = Column(Integer, nullable=False, default=0)
    status = Column(String(20), nullable=False, default="Active")
