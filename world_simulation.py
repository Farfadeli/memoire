from tools.calendar import Calendar
from human.human import Human
from geographics.countries import Countries


class World():
#Initialisation
    def __init__(self, human_nb_at_start: int, nb_countries: int, gap: int, limit: int):
        # Variable initiale de la simulation
        self.calendar = Calendar()
        self.human_number = human_nb_at_start
        self.countries_number = nb_countries
        self.gap = gap
        self.limit = limit

        self.human_list = []
        self.countries = Countries(self.countries_number)

        # Création des huamains de base dans la simulation
        for _ in range(self.human_number):
            self.human_list.append(
                Human(self.countries.get_random_countries(), self.calendar.get_date()))

        self.main_loop()

#-----------------------------------------------------------------------------------------------------------------------------------------
#Simulation loop

    def main_loop(self) -> None:
        """Boucle principale de la simulation"""
        year_number = self.limit*365
        while year_number > 0:
            self.logical_loop()
            self.couple_loop()
            self.died_loop()

            year_number -= self.gap

    def logical_loop(self) -> None:
        """Boucle princiaple pour ce qui arrrive à chaque pas de temps"""
        self.calendar.process_multiple_day(self.gap)

    def couple_loop(self) -> None:
        """Boucle principale pour la formation de couple entre 2 huamains"""
        for human in self.human_list:
            if self.calendar.get_year() - human.get_birth_year() >= 18:
                print(
                     f"name : {human.get_name()} can be in couple beaause {'he' if human.get_sexuality() == 'M' else 'she'} is {self.calendar.get_year() - human.get_birth_year()} years old")

    def died_loop(self) -> None:
        """Boucle principale pour la gestion de la mort des humains"""
        pass

#-----------------------------------------------------------------------------------------------------------------------------------------
#Getter

    def get_calendar(self) -> Calendar: return self.calendar
    def get_human_number(self) -> int: return self.human_number
    def get_human_list(self) -> list[Human]: return self.human_list
    def get_countries_list(self) -> list[Countries]: return self.countries
