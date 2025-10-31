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

        # Calculate sexual orientation (hetero - Homo - Bi)
        random_orientation = random.randint(0,100)
        self.sexual_orientation = "Hetero" if random_orientation < 91 else ('Bi' if random_orientation > 91 and random_orientation < 94 else 'Homo')

        self.in_couple = False
        self.couple_id  = ""
        self.human_couple = ''

        self.is_dead = False
        self.born_country = born_country
    
    def make_travel(self, countries_list : list[Country]) -> None:
        self.last_travel_country =  random.choice(countries_list)
        self.in_travel = True

        if self.get_in_couple(): 
            self.human_couple.set_last_travel_country(self.last_travel_country)
            self.human_couple.set_travel(True)


    
    def return_to_live_country(self) :
        self.in_travel = False
        if self.get_in_couple() :
            self.human_couple.set_travel(False)

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
    def get_in_couple(self) -> bool : return self.in_couple

    def set_couple_id(self, human_id : uuid.UUID) -> None : self.couple_id = human_id
    def set_human_couple(self, human : Human) -> None : self.human_couple = human
    def set_travel(self, value : bool) -> None : self.in_travel = value
    def set_last_travel_country(self, country : Country) -> None : self.last_travel_country = country