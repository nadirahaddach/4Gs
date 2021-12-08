import requests
from flask import Blueprint, render_template

app_starter = Blueprint('aboutus', __name__,
                        url_prefix='/',
                        template_folder='templates/aboutus/',
                        static_folder='static',
                        static_url_path='assets')



def population():
    url = "https://world-population.p.rapidapi.com/worldpopulation"

    headers = {
        'x-rapidapi-host': "world-population.p.rapidapi.com",
        'x-rapidapi-key': "4ead57fd33mshf1561aa23889096p18583ejsncb8b90ef517c"
    }

    response = requests.request("GET", url, headers=headers)

    factt = response.json()

    return render_template("/paigeapi.html", factt=factt)
