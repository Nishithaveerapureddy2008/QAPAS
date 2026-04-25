# record.py

import datetime

class Record:
    def __init__(self, rid):
        self.rid = rid
        self.time = datetime.datetime.now()

class Student(Record):
    def __init__(self, rid, name):
        super().__init__(rid)
        self.name = name

class Result(Record):
    def __init__(self, rid, score):
        super().__init__(rid)
        self.score = score