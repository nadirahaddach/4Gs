# import "packages" from flask
from flask import Flask, render_template, request
from templates.aboutus.briaapi import eightball
# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/nadira/')
def nadira():
    return render_template("aboutus/nadira.html")

@app.route('/bria/', methods=['GET', 'POST'])
def bria():
    return render_template("aboutus/bria.html")


@app.route('/briasapi/', methods=['GET', 'POST'])
def eightballapi():
    search = " "
    if request.form:
        prediction = request.form.get("eightballz")
        search = eightball(prediction)
        if len(prediction) != 0:  # input field has content
            print("Please enter an input")
        print(search)

    return render_template("aboutus/briasapi.html", fact=search)

@app.route('/jessie/')
def jessie():
    return render_template("aboutus/jessie.html")

@app.route('/paige/')
def paige():
    return render_template("aboutus/paige.html")

@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus/aboutus.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
