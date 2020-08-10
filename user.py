import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    born_date = Column(DateTime)
    gender = Column(String)

    def __init__(self, fullname, born_date, male):
        self.fullname = fullname
        self.born_date = born_date
        self.gender = male

    def __repr__(self):
        old = datetime.datetime.now().year - self.born_date.year
        return "User: <'%s','%s', '%s', '%s'>" % (self.fullname, self.born_date, self.gender, old)
