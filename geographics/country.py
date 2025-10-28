import random

class Country() : 
    
    def __init__(self) :
        self.name = random.choice(["France" , "Maroc", "Japon", "Allemagne", "Etats-unis", "Canada", "Chine", "Russie", "Egypte"])
    
    def get_country_name(self) -> str : return self.name