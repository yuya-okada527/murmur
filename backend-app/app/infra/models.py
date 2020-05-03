from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Sequence
)

from ..infra.database import Base


class Murmur(Base):
    __tablename__ = "murmur"

    id = Column(Integer, Sequence("murmur_id_seq"), primary_key=True)
    user_id = Column(String(8))
    user_name = Column(String)
    message = Column(String)
    time = Column(DateTime)


