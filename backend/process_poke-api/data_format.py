from typing import List, Dict, Literal, Tuple
from models.Pokemon import Pokemon, Types
from models.Ability import Ability
from models.Move import Move, Category
from models.Stat import Stat

def create_pokemon(pokemon: dict, pokemon_species: dict):
    id, dex_number = pokemon.get('id')
    names = pokemon_species.get('names', [])
    fr_name = next((n['name'] for n in names if n['language']['name'] == 'fr'), 'Unknown')
    base_exp = pokemon.get('base_experience', 0)
    height, weight = pokemon.get('height', 0), pokemon.get('weight', 0)
    types_data = [t.get("type", {}).get("name", "none") for t in pokemon.get("types", [{}])]
    types = Tuple(Types(t) if t in Types.__members__ else Types.none for t in types_data)

    abilities = [
        Ability(
            name=ability["ability"]["name"],
            description=f"Description for {ability['ability']['name']}",  # Placeholder
            is_hidden=ability.get("is_hidden", False),
        )
        for ability in pokemon.get("abilities", [])
    ]

    moves = [
        Move(
            name=move["move"]["name"],
            power=move.get("power", 0),
            accuracy=move.get("accuracy", 0),
            pp=move.get("pp", 0),
            type=move.get("type", {}).get("name", "unknown"),
            category=Category(move.get("category", "status"))  # Default to "status" if not provided
        )
        for move in pokemon.get("moves", [])
    ]

    stats = [Stat(name=stat["stat"]["name"], value=stat["base_stat"]) for stat in pokemon.get("stats", [])]
