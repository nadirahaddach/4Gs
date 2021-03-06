# import "packages" from flask
from flask import Flask, render_template, request
from __init__ import app
import requests
from image import image_data
from crud.app_crud import app_crud
from pathlib import Path
from crud.app_crud_api import app_crud_api

# create a Flask instance
app.register_blueprint(app_crud_api)
app.register_blueprint(app_crud)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")


@app.route('/nadira/')
def nadira():
    return render_template("aboutus/nadira.html")

@app.route('/nadirasapi', methods=['GET', 'POST'])
def nadirasapi():
    url = "https://sportscore1.p.rapidapi.com/sports/1/teams"
    querystring = {"page":"1"}
    headers = {
        'x-rapidapi-host': "sportscore1.p.rapidapi.com",
        'x-rapidapi-key': "a2dc907d76mshcd95463944ec47cp16d7a6jsn37846a41a807"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    # team_list = json.loads(response.json())
    # team_random = random.choice(team_list)
    # print(json.dumps(team_random))
    print(response.text)
    return render_template("aboutus/nadirasapi.html", sport=response.json())


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

@app.route('/paigeapi/', methods=['GET', 'POST'])
def population():
    url = "https://world-population.p.rapidapi.com/worldpopulation"
    headers = {
        'x-rapidapi-key': "4ead57fd33mshf1561aa23889096p18583ejsncb8b90ef517c",
        'x-rapidapi-host': "world-population.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    stats = response.json()
    pop = stats['body']['world_population']
    return render_template("aboutus/paigeapi.html", stats=pop)


@app.route('/mathpage/')
def mathpage():
    return render_template("math.html")


@app.route('/sportspage/')
def sportspage():
    return render_template("sportspage.html")


@app.route('/comment/')
def comment():
    return render_template("comment.html")

@app.route('/councelorsearch/', methods=['GET', 'POST'])
def councelorsearch():
    if request.form:
        input = request.form.get("lname")
        print("works")
        if len("input") != 0:
            return render_template("councelorsearch.html", input=input)
    return render_template("councelorsearch.html")


@app.route('/clubpage/')
def clubpage():
    return render_template("clubpage.html")

@app.route('/map2/')
def map2():
    return render_template("map2.html")

@app.route('/gpa/')
def gpa():
    return render_template("gpa.html")

@app.route('/maptest/')
def maptest():
    return render_template("maptest.html")

@app.route('/nadirargb/', methods=["GET", "POST"])
def nadirargb():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('nadirargb.html', images=image_data(path))


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)