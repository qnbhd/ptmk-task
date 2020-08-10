from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    born_date = Column(Date)
    gender = Column(String(1))

    def __init__(self, fullname, born_date, male):
        self.fullname = fullname
        self.born_date = born_date
        self.gender = male

    @staticmethod
    def age(dob):
        import datetime
        today = datetime.date.today()

        if today.month < dob.month or \
                (today.month == dob.month and today.day < dob.day):
            return today.year - dob.year - 1
        else:
            return today.year - dob.year

    def __repr__(self):
        old = self.age(self.born_date)
        return "User: <'%s','%s', '%s', '%s'>" % (self.fullname,
                                                  self.born_date,
                                                  'male' if self.gender == 'm' else 'female', old)
