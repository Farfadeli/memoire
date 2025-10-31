from human.human import Human
from geographics.country import Country
import uuid

class Couple() :
    def __init__(self, first_human : Human, second_human : Human) :
        self.couple_id = uuid.uuid4()
        self.first : Human = first_human
        self.second : Human = second_human

    def make_child(self , country : Country, date : str) -> dict:
        # Vérification si le couple est homosexuel
        if self.first.get_sexuality() == self.second.get_sexuality() :
            return {'child' : Human(country, date), 'response' : False}
        else :
            return {'child' : Human(country, date), 'response' : True}
    
    def get_couple_country(self) :
        return self.first.get_country()

    def adopt_child(self) -> dict :
        return {'child' : '', 'response' : False}

    def make_in_couple(self) :
        self.first.set_couple_id(self.second.get_id())
        self.second.set_couple_id(self.first.get_id())
    def get_id(self) -> uuid.UUID : return self.couple_id
    def get_first(self) -> Human : return self.first
    def get_second(self) -> Human : return self.second
    def get_couple(self) -> list[Human] : return [self.first, self.second]