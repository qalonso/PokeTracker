class Pokemon:
    def __init__(self, dex: int, nom: str, hauteur: int, poids: int):
        self.id = dex
        self.nom = nom
        self.hauteur = hauteur
        self.poids = poids
        self.talents = []
        self.types = []
        self.statistiques = {
            "pv": 0,
            "attaque": 0,
            "defense": 0,
            "attaque_speciale": 0,
            "defense_speciale": 0,
            "vitesse": 0
        }
        
    class Talent:
        _instances = {}
        
        def __new__(cls, nom):
            if nom in cls._instances:
                return cls._instances[nom]
            
            instance = super().__new__(cls)
            cls._instances[nom] = instance
            return instance
        
        def __init__(self, nom: str):
            self.nom = nom
            self.description = ""
            self.effets = {}
            
        def ajouter_description(self, description: str):
            self.description = description
            
        def ajouter_effet(self, ou: str, effet: str):
            self.effets[ou] = effet
        
    def add_talent(self):
        pass
        
    def add_types(self, nom: str):
        pass