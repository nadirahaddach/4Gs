import requests

def population():
    url = "https://world-population.p.rapidapi.com/worldpopulation"
    headers = {
        'x-rapidapi-key': "4ead57fd33mshf1561aa23889096p18583ejsncb8b90ef517c",
        'x-rapidapi-host': "world-population.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    stats = response.json()
    print(stats)
    pop = stats['body']['world_population']
    print(pop)


population()
