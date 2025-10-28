from geographics.country import Country
import random


class Countries() :
    
    def __init__(self, nb_country_in_simulation : int) : 
        self.world_countries = []
        for _ in range(nb_country_in_simulation) :
            selected_country = Country()
            while selected_country in self.world_countries :
                selected_country = Country()
            self.world_countries.append(selected_country)

    def get_random_countries(self) -> Country :
        return random.choice(self.world_countries)
    def get_country(self) -> list[Country] : return self.world_countries