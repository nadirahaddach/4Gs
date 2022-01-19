"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api, Resource
import requests

from model import Comments

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_crud = Blueprint('crud', __name__,
                     url_prefix='/crud',
                     template_folder='/templates/',
                     static_folder='static',
                     static_url_path='assets')


# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_crud)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Blueprint)
    3.) API routes
    4.) API testing
"""

""" Users table queries"""


# User/Users extraction from SQL
def comments_all():
    """converts Users table into JSON list """
    return [peep.read() for peep in Comments.query.all()]


def comments_ilike(term):
    """filter Users table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Comments.query.filter((Comments.name.ilike(term)))
    return [peep.read() for peep in table]


# User extraction from SQL
def comment_by_id(commentid):
    """finds User in table matching userid """
    return Comments.query.filter_by(commentID=commentid).first()


# User extraction from SQL


""" app route section """


# Default URL
@app_crud.route('/')
def crud():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crud.html", table=comments_all())


# CRUD create/add
@app_crud.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Comments (
            request.form.get("name"),
            request.form.get("date"),
            request.form.get("grade"),
            request.form.get("comment")
        )
        po.create()
    return redirect(url_for('crud.crud'))


# CRUD read
@app_crud.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        commentid = request.form.get("commentid")
        po = user_by_id(commentid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("crud.html", table=table)


# CRUD update
@app_crud.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        commentid = request.form.get("commentid")
        name = request.form.get("name")
        po = user_by_id(userid)
        if po is not None:
            po.update(name)
    return redirect(url_for('crud.crud'))


# CRUD delete
@app_crud.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        commentid = request.form.get("commentid")
        po = user_by_id(commentid)
        if po is not None:
            po.delete()
    return redirect(url_for('crud.crud'))


# Search Form
@app_crud.route('/search/')
def search():
    """loads form to search Users data"""
    return render_template("search.html")


# Search request and response
@app_crud.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(comments_ilike(term)), 200)
    return response


""" API routes section """


class CommentsAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, name, date, grade, comment):
            po = Comments(name, date, grade, comment)
            person = po.create()
            if person:
                return person.read()
            return {'message': f'Processed {name}, a format error'}, 210

    # class for read/get
    class _Read(Resource):
        def get(self):
            return comments_all()

    # class for read/get
    class _ReadILike(Resource):
        def get(self, term):
            return comments_ilike(term)

    # class for update/put
    class _Update(Resource):
        def put(self, name):
            po.update(name)
            return po.read()

    class _UpdateAll(Resource):
        def put(self, name, date, grade, comment):
            po.update(name, date, grade, comment)
            return po.read()

    # class for delete
    class _Delete(Resource):
        def delete(self, commentid):
            po = comment_by_id(commentid)
            if po is None:
                return {'message': f"{commentid} is not found"}, 210
            data = po.read()
            po.delete()
            return data

    # building RESTapi resource
    api.add_resource(_Create, '/create/<string:name>/<string:date>/<string:grade>/<string:comment>')
    api.add_resource(_Read, '/read/')
    api.add_resource(_ReadILike, '/read/ilike/<string:term>')
    api.add_resource(_Update, '/update/<string:name>')
    api.add_resource(_UpdateAll, '/update/<string:name>/<string:date>/<string:grade>/<string:comment>')
    api.add_resource(_Delete, '/delete/<int:userid>')


""" API testing section """


def api_tester():
    # local host URL for model
    url = 'http://localhost:5222/crud'

    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/create/Wilma Flintstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/create/Fred Flintstone/fred@bedrock.org/123wifli/0001112222', "post"],
        ['/read/', "get"],
        ['/read/ilike/John', "get"],
        ['/read/ilike/com', "get"],
        ['/update/wilma@bedrock.org/Wilma S Flintstone/123wsfli/0001112229', "put"],
        ['/update/wilma@bedrock.org/Wilma Slaghoople Flintstone', "put"],
        ['/delete/4', "delete"],
        ['/delete/5', "delete"],
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {url + test[API]})")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")


def api_printer():
    print()
    print("Users table")
    for comment in comments_all():
        print(comment)


"""validating api's requires server to be running"""
if __name__ == "__main__":
    api_tester()
    api_printer()