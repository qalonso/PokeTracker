from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Pokemon import Pokemon
from models.Move import Move

from database_models.DB_Pokemon import Base, PokemonDB



# Configuration de la base de données
DATABASE_URL = "sqlite:///./test.db"
database = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=database)

# Créer les tables dans la base de données
Base.metadata.create_all(bind=database)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/pokemon")
async def create_pokemon(pokemon: Pokemon):
    return pokemon

@app.post("/move")
async def create_move(move: Move):
    return move

@app.get("/pokemon/{dex_number}", response_model=Pokemon)
async def get_pokemon_dex_number(dex_number: int, db: SessionLocal = Depends(get_db)):
    pokemon = db.query(PokemonDB).filter(PokemonDB.natdex == dex_number).first()
    if pokemon:
        return Pokemon(
            id=pokemon.id,
            natdex=pokemon.natdex,
            name=pokemon.name,
            types=(pokemon.type1, pokemon.type2),
            abilities=[],  # Remplacez par les données réelles
            stats=[],  # Remplacez par les données réelles
            moves=[],  # Remplacez par les données réelles
            egg_groups=[],
            egg_cycles=0,
            catch_rate=0,
            gender_ratio=(0, 0),
            base_exp=0,
            sprites={"normal": "", "shiny": ""},
            height=0,
            weight=0,
            home_dex_entry="",
            evolution_line={}
        )
    raise HTTPException(status_code=404, detail="Pokémon not found")