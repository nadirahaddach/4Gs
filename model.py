""" database dependencies to support Users db examples """
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate

from __init__ import app

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
# Define variable to define type of database (sqlite), and name and location of myDB.db
dbURI = 'sqlite:///model/myDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Users(db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    grade = db.Column(db.String(255), unique=False, nullable=False)
    advice = db.Column(db.String(255), unique=False, nullable=False)
    counselor = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, grade, advice, counselor):
        self.name = name
        self.grade = grade
        self.advice = advice
        self.counselor = counselor

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
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
            "advice": self.advice,
            "counselor": self.counselor
        }

    # CRUD update: updates users name, password, grade
    # returns self
    def update(self, name, grade="", advice=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(grade) > 0:
            self.grade = grade
        if len (advice) > 0:
            self.advice = advice
        if len(counselor) > 0:
            self.counselor = counselor
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
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Users(name='Thomas Edison', grade="12", advice='hello', counselor='')
    u2 = Users(name='Nicholas Tesla', grade="11", advice='hhello', counselor='')
    u3 = Users(name='Alexander Graham Bell', grade="09", advice='chello', counselor='')
    u4 = Users(name='Eli Whitney', grade="10", advice='shello', counselor='')
    u5 = Users(name='John Mortensen', grade="11", advice='dhello', counselor='')
    u6 = Users(name='John Mortensen', grade="12", advice='dhello', counselor='')
    # U7 intended to fail as duplicate key
    u7 = Users(name='John Mortensen', grade="11", advice='dhello', counselor='')
    table = [u1, u2, u3, u4, u5, u6, u7]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist")


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()