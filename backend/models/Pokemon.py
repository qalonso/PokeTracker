from typing import List, Dict, Literal, Tuple
from enum import Enum
from pydantic import BaseModel
from models.Ability import Ability
from models.Move import Move
from models.Stat import Stat

class Types(str, Enum):
    normal = "normal"
    fire = "fire"
    water = "water"
    electric = "electric"
    grass = "grass"
    ice = "ice"
    fighting = "fighting"
    poison = "poison"
    ground = "ground"
    flying = "flying"
    psychic = "psychic"
    bug = "bug"
    rock = "rock"
    ghost = "ghost"
    dragon = "dragon"
    dark = "dark"
    steel = "steel"
    fairy = "fairy"
    none = None

class Pokemon(BaseModel):
    id: int
    natdex: int # NatDex du pokemon
    name: str # Nom du pokemon en français
    types: Tuple[Types, Types] # Types du pokemon
    abilities: List[Ability] # Abilities du pokemon
    stats: List[Stat] # Stats du pokemon
    moves: List[Move] # Moves du pokemon
    egg_groups: List[str] # EggGroups du pokemon
    egg_cycles: int # EggCycles du pokemon > 1 cycle = 256 pas
    catch_rate: int # CatchRate du pokemon
    gender_ratio: Tuple[int, int] # Ratio de genre
    base_exp: int # BaseExp du pokemon
    sprites: Dict[Literal['normal', 'shiny'], str] # Sprites du pokemon, clés : 'normal', 'shiny'
    height: int # Taille du pokemon en dm > 1 = 0.1 m
    weight: int # Poids du pokemon en kg
    home_dex_entry: str # Entree Dex National
    evolution_line: Dict[str, str] # Ligne d'evolution Pokemon: Moyen d'evolution
    # forms: List[Pokemon] # Formes alternatives du pokemon
    
    def __str__(self):
        return f""