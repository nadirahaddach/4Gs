import requests


def eightball(prediction):
    url = "https://magic-8-ball1.p.rapidapi.com/my_answer/"

    question = str(prediction)
    querystring = {"question": question}

    headers = {
        'x-rapidapi-host': "magic-8-ball1.p.rapidapi.com",
        'x-rapidapi-key': "435f957ca1msh508be3bb9ed13fap1d89c7jsn47a12462048a"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json().get('answer')
