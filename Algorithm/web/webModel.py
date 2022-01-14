from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate

from __init__ import app

dbURI = 'sqlite:///model/websiteDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)


class webPages(db.Model):
    pageID = db.Column(db.Integer, primary_key=True)
    pageName = db.Column(db.String(255), unique=False, nullable=False)
    pageURL = db.Column(db.String(255), unique=True, nullable=False)
    pageDesc = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, pageName, pageURL, pageDesc):
        self.pageName = pageName
        self.pageURL = pageURL
        self.pageDesc = pageDesc

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def read(self):
        return {
            "pageID": self.pageID,
            "pageName": self.pageName,
            "pageURL": self.pageURL,
            "pageDesc": self.pageDesc
        }

    def update(self, pageName, pageURL='', pageDesc=''):
        if len(pageName) > 0:
            self.pageName = pageName
        if len(pageURL) > 0:
            self.pageURL = pageURL
        if len(pageDesc) > 0:
            self.pageDesc = pageDesc
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


def model_tester():
    db.create_all()
    p1 = webPages(pageName='Math PATH', pageURL='http://127.0.0.1:5000/Math_Path/')
    table = [p1]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records already exist: {row.pageURL}")

def model_printer():
    print("------------")
    print("Table: webpages with SQL query")
    print("------------")
    result = db.session.execute('select * from webPages')
    print(result.keys())
    for row in result:
        print(row)

if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()