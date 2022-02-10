""" database dependencies to support Gpadata db examples """
from sqlalchemy.exc import IntegrityError
from __init__ import db

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along


# Define the Gpadata table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Gpadata represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Gpadata(db.Model):
    # define the Gpadata schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    grade = db.Column(db.String(255), unique=True, nullable=False)
    gpa = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, grade, gpa):
        self.name = name
        self.grade = grade
        self.gpa = gpa

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Gpadata(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Gpadata table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "grade": self.grade,
            "gpa": self.gpa,
            "query": "by_alc"  # This is for fun, a little watermark
        }

    # CRUD update: updates Gpadata name, gpa, phone
    # returns self
    def update(self, name, grade="", gpa=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(grade) > 0:
            self.grade = grade
        if len(gpa) > 0:
            self.gpa = gpa
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: Gpadata")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Gpadata(name='Thomas Edison', grade='tedison@example.com', gpa='123toby')
    u2 = Gpadata(name='Nicholas Tesla', grade='ntesla@example.com', gpa='123niko')
    u3 = Gpadata(name='Alexander Graham Bell', grade='agbell@example.com', gpa='123lex')
    u4 = Gpadata(name='Eli Whitney', grade='eliw@example.com', gpa='123whit')
    u5 = Gpadata(name='John Mortensen', grade='jmort1021@gmail.com', gpa='123qwerty')
    u6 = Gpadata(name='John Mortensen', grade='jmort1021@yahoo.com', gpa='123qwerty')
    # U7 intended to fail as duplicate key
    u7 = Gpadata(name='John Mortensen', grade='jmort1021@yahoo.com', gpa='123qwerty')
    table = [u1, u2, u3, u4, u5, u6, u7]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate grade, or error: {row.grade}")


def model_printer():
    print("------------")
    print("Table: Gpadata with SQL query")
    print("------------")
    result = db.session.execute('select * from Gpadata')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Gpadata
    model_printer()