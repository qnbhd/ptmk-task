import datetime
import os
import random
import string
import benchmark

from typing import List, Tuple
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import Base, User

SQLDEBUG = False
FILENAME = 'ptmk'
GENERATE_COUNT = 1000


class PtmkWorker:

    def __init__(self):
        self.engine = create_engine(f'sqlite:///{FILENAME}.db', echo=SQLDEBUG)

    def create_bd_handler(self, **kwargs):
        if os.path.isfile(f'{FILENAME}.db'):
            os.remove(f'{FILENAME}.db')
        Base.metadata.create_all(self.engine)

    def create_session(self):
        return sessionmaker(bind=self.engine)()

    @staticmethod
    def join_by_gaps(fullname: List[str]):
        return ' '.join(fullname)

    @staticmethod
    def create_record_instance(fullname: str,
                               born_date: str, gender: str) -> User:
        born_date_inst = datetime.datetime. \
            strptime(born_date, "%d.%m.%Y")  # simplification
        return User(fullname, born_date_inst, gender)

    @staticmethod
    def validate_gender(gender: str):
        return gender in ['f', 'm']

    def create_record_handler(self, fullname: List[str],
                              born_date: str, gender: str):
        session = self.create_session()
        user_inst = self.create_record_instance(self.join_by_gaps(fullname),
                                                born_date, gender)
        if not self.validate_gender(gender):
            raise ValueError("Gender must be 'f' - female or 'm' - male")

        session.add(user_inst)
        session.commit()

    def out_unique_records_handler(self, **kwargs):
        session = self.create_session()
        instances = session.query(User). \
            distinct(User.fullname + User.born_date).order_by(User.fullname)
        for instance in instances:
            print(instance)

    @staticmethod
    def get_random_lit() -> str:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(9))

    @staticmethod
    def get_random_record(gen=None) -> Tuple[str, str, str]:
        gender = random.choice(('f', 'm'))

        fullname = ''

        if gen is not None:
            fullname = 'F'
            gender = 'm'

        fullname += (PtmkWorker.get_random_lit().capitalize() + " " +
                     PtmkWorker.get_random_lit().capitalize() + " " +
                     PtmkWorker.get_random_lit().capitalize())

        born_date = (str(random.randrange(1, 28)) + "." +
                     str(random.randrange(1, 12)) + "." +
                     str(random.randrange(1970, 2020)))

        return fullname, born_date, gender

    def random_creator_handler(self, **kwargs):
        records = [self.get_random_record(gen='special') for _ in range(100)]
        records += [self.get_random_record() for _ in range(GENERATE_COUNT)]

        session = self.create_session()

        for fullname, born_date, gender in records:
            new_user = self.create_record_instance(fullname, born_date, gender)
            session.add(new_user)

        session.commit()

    @benchmark.bench
    def sample_handler(self, **kwargs):
        session = self.create_session()
        search = "F%"
        result = session.query(User) \
            .filter_by(gender="m") \
            .filter(User.fullname.like(search)) \
            .all()
        for record in result:
            print(record)

    def out_first_records(self, records_count=10):
        """
        Print first 'records_count' records in database
        :param records_count:
        :return: -
        """
        session = self.create_session()
        instances = session.query(User).all()[:records_count]
        for instance in instances:
            print(instance)
