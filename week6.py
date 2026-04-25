# student.py

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

class Quiz:
    def __init__(self, subject):
        self.subject = subject

class Result:
    def __init__(self, sid, score):
        self.sid = sid
        self.score = score