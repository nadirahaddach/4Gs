import requests
from flask import Blueprint, render_template, request
import base64
import random

from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

app_map = Blueprint('map', __name__,
                        url_prefix='/map',
                        template_folder='templates/map/',
                        static_folder='static',
                        static_url_path='/static/assets/map')


@app_map.route('/mapgeoguesser')
def mapgeoguesser():
    img_list = ['/dnfield.png',
                '/dngym.png',
                '/dnoffice.png',
                '/dnpool.png',
                '/dnquad.png']
    img_choice = random.choice(img_list)
    with open(img_choice, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return render_template('mapgeoguesser.html', htmlimg_base = my_string)

if __name__ == '__main__':
    app.run()
