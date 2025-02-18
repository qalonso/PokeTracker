import json
import requests

# URL de l'API pour récupérer les informations sur Pikachu
url = "https://pokeapi.co/api/v2/pokemon/25" # numero dex pikachu = 25
url2 = "https://pokeapi.co/api/v2/pokemon-species/25"
url3 = "https://pokeapi.co/api/v2/pokemon/25/encounters"

# Faire une requête GET à l'API
pokemon = requests.get(url)
pokemon_species = requests.get(url2)
pokemon_encounters = requests.get(url3)
    
with open('pokemon.json', 'w') as f:
    json.dump(pokemon.json(), f)
with open('pokemon-species.json', 'w') as f:
    json.dump(pokemon_species.json(), f)
with open('pokemon-encounters.json', 'w') as f:
    json.dump(pokemon_encounters.json(), f)