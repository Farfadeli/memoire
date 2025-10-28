class Calendar() :
    
    def __init__(self) :
        self.day, self.month, self.year = 1, 1, 1970
    
    def is_leap_year(self) -> bool: return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)
    
    def process_day(self) -> None:
        max_day = 31 if self.month in [1,3,5,7,8,10,12] else (30 if  self.month in [4,6,9,11] else (29 if self.is_leap_year() else 28))
        self.day += 1
        if self.day > max_day :
            self.day = 1
            if self.month == 12 :
                self.month = 1
                self.year += 1
            else :
                self.month += 1
            
            
    def process_multiple_day(self, nb_days : int) :
        for _ in range(nb_days) : self.process_day()
    
    def get_date(self) -> str :
        return f"{self.day}/{self.month}/{self.year}"
    def get_year(self) -> int : return self.year