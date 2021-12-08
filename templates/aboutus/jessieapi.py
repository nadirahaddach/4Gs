import random

from flask import Blueprint, jsonify

app_api = Blueprint('api', __name__,
                    url_prefix='/api',
                    template_folder='templates',
                    static_folder='static', static_url_path='static/api')

fortunes_data = []
fortune_list = [
    "A lifetime of happiness lies ahead of you. "
    "You love challenge.",
    "Your ability is appreciated.",
    "Your mind is your greatest asset.",
    "Your life will get more and more exciting.",
    "Your mentality is alert, practical, and analytical.",
    "Your moods signal a period of change.",
    "A new perspective will come with the new year. "
    "A golden egg of opportunity falls into your lap this month.",
    "A gambler not only will lose what he has, but also will lose what he doesn’t have.",
    "Something is looking up to you. Don't let that person down.",
    "Run.",
    "Just have fun.",
    "Take care of yourself first. Then help others.",
    "Pay attention to your family, don't take them for granted.",
    "Purple is your lucky color today.",
    "Yellow is your color today.",
    "Be careful of your surroundings.",
    "Beware.",
]


def _init_fortunes():
    item_id = 1
    for item in fortune_list:
        fortunes_data.append({"id": item_id, "fortune": item, "haha": 0, "boohoo": 0})
        item_id += 1


@app_api.route('/jessiesapi')
def fortune():
    if len(fortunes) == 0:
        _init_fortunes()
    return jsonify(random.choice(fortunes_data))


def fortunes():
    if len(fortunes_data) == 0:
        _init_fortunes()
    return jsonify(fortunes_data)


if __name__ == "__main__":
    print(random.choice(fortune_list))