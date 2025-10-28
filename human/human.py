import random
from human.utils import generate_random_name
from geographics.country import Country

class Human()  :
    
    def __init__(self, born_country : Country , birth_date : str) :
        self.sexe = random.choice(['F', 'M'])
        self.name = generate_random_name(self.sexe)
        self.birth_date = birth_date
        self.want_stranger = random.choice([True, False])
        
        self.is_dead = False
        self.country = born_country
    
    def get_sexuality(self) -> chr : return self.sexe
    def get_name(self) -> str : return self.name
    def get_country(self) -> Country : return self.country
    
    def get_birth_date(self) -> str : return self.birth_date
    def get_birth_year(self) -> int : return int(self.birth_date.split("/")[-1])
    
    def get_want_stanger(self) -> bool: return self.want_stranger
    def get_is_dead(self) -> bool : return self.is_dead