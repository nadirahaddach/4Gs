import requests

def recipe():
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/images/analyze"

    querystring = {"imageUrl":"https://spoonacular.com/recipeImages/635350-240x150.jpg"}

    headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "b8ff06ff0emsheb30cad1d33841fp1309bcjsn61e1b6e316de"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)