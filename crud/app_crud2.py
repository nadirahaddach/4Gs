"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response

from crud.sql import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_crud = Blueprint('crud', __name__,
                     url_prefix='/crud',
                     template_folder='templates/crud/',
                     static_folder='static',
                     static_url_path='static')

""" Application control for CRUD is main focus of this File, key features:
    1.) Gpadata table queries
    2.) app routes for CRUD (Blueprint)
"""


# Default URL
@app_crud.route('/')
def crud():
    """obtains all Gpadatas from table and loads Admin Form"""
    return render_template("crudtemp.html", table=Gpadatas_all())


# CRUD create/add
@app_crud.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Gpadatas table"""
    if request.form:
        po = Gpadatas(
            request.form.get("name"),
            request.form.get("grade"),
            request.form.get("gpa")
        )
        po.create()
    return redirect(url_for('crud.crudtemp'))


# CRUD read
@app_crud.route('/read/', methods=["POST"])
def read():
    """gets Gpadataid from form and obtains corresponding data from Gpadatas table"""
    table = []
    if request.form:
        Gpadataid = request.form.get("Gpadataid")
        po = Gpadata_by_id(Gpadataid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("crudtemp.html", table=table)


# CRUD update
@app_crud.route('/update/', methods=["POST"])
def update():
    """gets Gpadataid and name from form and filters and then data in  Gpadatas table"""
    if request.form:
        Gpadataid = request.form.get("Gpadataid")
        name = request.form.get("name")
        po = Gpadata_by_id(Gpadataid)
        if po is not None:
            po.update(name)
    return redirect(url_for('crud.crudtemp'))


# CRUD delete
@app_crud.route('/delete/', methods=["POST"])
def delete():
    """gets Gpadataid from form delete corresponding record from Gpadatas table"""
    if request.form:
        Gpadataid = request.form.get("Gpadataid")
        po = Gpadata_by_id(Gpadataid)
        if po is not None:
            po.delete()
    return redirect(url_for('crud.crudtemp'))


# Search Form

