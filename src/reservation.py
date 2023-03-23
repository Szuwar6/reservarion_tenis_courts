class Reservation:
    def __init__(self, name: str, start_date: str, end_date: str):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_week = start_date.isocalendar()[1]

    def __eq__(self, other):
        return (self.name, self.start_date, self.end_date, self.number_of_week) == (
            other.name,
            other.start_date,
            other.end_date,
            other.number_of_week,
        )

    def display(self):
        print(
            f'{self.name}, {self.start_date.strftime("%d.%m.%Y %H:%M")} - {self.end_date.strftime("%d.%m.%Y %H:%M")}'
        )
