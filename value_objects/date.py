class Date:
    def __init__(self, *, day: int = 1, month: int = 1, year: int = 0):
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError("day, month and year must be integers")
        
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 0:
            raise TypeError("the date is invalid")
        
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"{self.day:02d}/{self.month:02d}/{self.year}"