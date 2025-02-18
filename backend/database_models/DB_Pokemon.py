from sqlalchemy import Column, Integer, String, Enum as SQLAlchemyEnum, PickleType
from sqlalchemy.ext.declarative import declarative_base
from typing import List, Tuple, Dict, Literal
from models.Pokemon import Types

Base = declarative_base()

class PokemonDB(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True, index=True)
    natdex = Column(Integer, index=True)
    name = Column(String, index=True)
    type1 = Column(SQLAlchemyEnum(Types))
    type2 = Column(SQLAlchemyEnum(Types))
    abilities = Column(PickleType)  # Stocké comme une liste de dictionnaires
    stats = Column(PickleType)  # Stocké comme une liste de dictionnaires
    moves = Column(PickleType)  # Stocké comme une liste de dictionnaires
    egg_groups = Column(PickleType)  # Stocké comme une liste de chaînes
    egg_cycles = Column(Integer)
    catch_rate = Column(Integer)
    gender_ratio = Column(PickleType)  # Stocké comme un tuple
    base_exp = Column(Integer)
    sprites = Column(PickleType)  # Stocké comme un dictionnaire
    height = Column(Integer)
    weight = Column(Integer)
    home_dex_entry = Column(String)
    evolution_line = Column(PickleType)  # Stocké comme un dictionnaire
