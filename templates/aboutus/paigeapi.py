import requests
from flask import Blueprint, render_template, request

from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

app_starter = Blueprint('starter', __name__,
                        url_prefix='/starter',
                        template_folder='templates/',
                        static_folder='static',
                        static_url_path='assets')


@app_starter.route('/paigeapi', methods=['GET', 'POST'])
def population():

    url = "https://world-population.p.rapidapi.com/worldpopulation"

    headers = {
        'x-rapidapi-host': "world-population.p.rapidapi.com",
        'x-rapidapi-key': "4ead57fd33mshf1561aa23889096p18583ejsncb8b90ef517c"
    }

    response = requests.request("GET", url, headers=headers)
    factt = response.json().get('world_population')
    return render_template("paigeapi.html", factt=factt)

print(response.text)