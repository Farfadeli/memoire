from human.human import Human
from geographics.country import Country
import uuid

class Couple() :
    def __init__(self, first_human : Human, second_human : Human) :
        self.couple_id = uuid.uuid4()
        self.first : Human = first_human
        self.second : Human = second_human

    def make_child(self , country : Country, date : str) -> Human:
        # Vérification si le couple est homosexuel
        if self.first.get_sexuality() == self.second.get_sexuality() :
            pass
        else :
            return Human(country , date)
    

    def get_id(self) -> uuid.UUID : return self.couple_id