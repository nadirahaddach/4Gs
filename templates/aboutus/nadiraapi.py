import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

sports = []
sports_list = [
    "Cross Country", "Feild Hockey", "Football", "Golf", "Tennis", "Volleyball",
    "Water Polo", "Basketball", "Cheer", "Roller Hcokey", "Soccer", "Wrestling", "Badminton", "Baseball",
    "Gymnastics", "Lacrosse", "Softball", "Swimming and Diving", "Track and Feild",
    "Beach Volleyball"
]


def _find_next_id():
    return max(sports["id"] for sport in sports) + 1


def _init_sports():
    id = 1
    for sport in sports_list:
        sports.append({"id": id, "sport": sport, "haha": 0, "boohoo": 0})
        id += 1


@api_bp.route('/nadirasapi')
def get_sport():
    if len(sports) == 0:
        _init_sports()
    return jsonify(random.choice(sports))


if __name__ == "__main__":
    print(random.choice(sports_list))