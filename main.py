# import "packages" from flask
from flask import render_template, request
import requests
from templates.aboutus.briaapi import eightball
from crud.app_crud import app_crud
from __init__ import app


# create a Flask instance
app.register_blueprint(app_crud)

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


@app.route('/paige/')
def paige():
    return render_template("aboutus/paige.html")

@app.route('/clubs/')
def clubs():
    return render_template("clubpage.html")

@app.route('/math/')
def math():
    return render_template("math.html")

@app.route('/homepage/')
def homepage():
    return render_template("homepage.html")


@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus/aboutus.html")

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

@app.route('/JessieAboutMe/')
def JessieAboutMe():
    return render_template("JessieAboutMe.html")

@app.route('/Math_Path/')
def Math_Path():
    return render_template("Math_Path.html")

@app.route('/map2/')
def map2():
    return render_template("map2.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)