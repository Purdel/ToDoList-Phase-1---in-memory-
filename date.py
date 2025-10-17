class Date:
    def __init__(self, *, day: int = 1, month: int = 1, year: int = 0):
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError("day, month and year must be integers")
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 0:
            raise TypeError("the date is invalid")
        self._day = int(day)
        self._month = int(month)
        self._year = int(year)

    # day getter / setter
    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, new_day: int):
        if not isinstance(new_day, int):
            raise TypeError("day must be an integer")
        if new_day < 1 or new_day > 31:
            raise TypeError("invalid day")
        self._day = new_day

    # month getter / setter
    @property
    def month(self) -> int:
        return self._month

    @month.setter
    def month(self, new_month: int):
        if not isinstance(new_month, int):
            raise TypeError("month must be an integer")
        if new_month < 1 or new_month > 12:
            raise TypeError("invalid month")
        self._month = new_month

    # year getter / setter
    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, new_year: int):
        if not isinstance(new_year, int):
            raise TypeError("year must be an integer")
        if new_year < 0:
            raise TypeError("invalid year")
        self._year = new_year

    def __str__(self) -> str:
        return f"{self._day:02d}/{self._month:02d}/{self._year}"

    def show(self) -> None:
        print(str(self))