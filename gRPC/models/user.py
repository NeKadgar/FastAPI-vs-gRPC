from sqlalchemy import Column, Integer, String, CheckConstraint

from .db import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    age = Column(Integer)

    __table_args__ = (
        CheckConstraint(age >= 0, name='check_bar_positive'),
        {}
    )

def migrate():
    pass