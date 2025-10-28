import random
from human.utils import generate_random_name
from geographics.country import Country
import uuid

class Human()  :
    
    def __init__(self, born_country : Country , birth_date : str) :
        self.human_id = uuid.uuid4()

        self.sexe = random.choice(['F', 'M'])
        self.name = generate_random_name(self.sexe)
        self.birth_date = birth_date
        self.want_stranger = random.choice([True, False])

        self.last_travel_country = born_country
        self.live_country = born_country
        self.in_travel = False

        self.is_dead = False
        self.born_country = born_country
    
    def make_travel(self, countries_list : list[Country]) -> None:
       self.last_travel_country =  random.choice(countries_list)
       self.in_travel = True
    
    def return_to_live_country(self) :
        self.in_travel = False

    def change_country(self, country : Country) :
        self.live_country = Country

    def get_sexuality(self) -> chr : return self.sexe
    def get_name(self) -> str : return self.name
    def get_country(self) -> Country : 
        if self.in_travel : return self.last_travel_country
        else : return self.live_country
    def get_born_country(self) -> Country :
        return self.born_country
    
    def get_birth_date(self) -> str : return self.birth_date
    def get_birth_year(self) -> int : return int(self.birth_date.split("/")[-1])
    
    def get_want_stanger(self) -> bool: return self.want_stranger
    def get_is_dead(self) -> bool : return self.is_dead

    def get_id(self) -> uuid.UUID : return self.human_id