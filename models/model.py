from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Mahasiswa(Base):
    __tablename__ = "mahasiswa"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String)
    ipk = Column(Float)
    sks = Column(Integer)
    status_kelulusan = Column(String)
    created_at = Column(DateTime, default=datetime.now)
