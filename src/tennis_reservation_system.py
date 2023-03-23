import datetime

from src.reservation import Reservation
from src.schedule import Schedule


class TennisReservationSystem:
    def __init__(self):
        self.schedule = Schedule()

    def run(self):
        while True:
            action = input(
                "What do you want to do:\n1. Make a reservation\n2. Cancel a reservation\n"
                "3. Print schedule\n4. Save schedule to a file\n5. Exit\n")

            if action == "1":
                self.make_reservation()
            elif action == "2":
                self.cancel_reservation()
            elif action == "3":
                self.print_schedule()
            elif action == "4":
                self.save_schedule()
            elif action == "5":
                break
            else:
                print("Invalid action. Please try again.\n")

    def make_reservation(self):
        name = input("Enter your name: ")
        while True:
            date_str = input("Enter date: {DD.MM.YYYY HH:MM}: ")
            try:
                start = datetime.datetime.strptime(date_str, "%d.%m.%Y %H:%M")
                if start.minute not in [0, 30]:
                    print("Booking start at full hour or half hour")
                    continue
                if start < datetime.datetime.now():
                    print("The entered date has already passed.")
                    continue
                if start < datetime.datetime.now() + datetime.timedelta(minutes=60):
                    print("Less than an hour to the start of the game, please choose another time.")
                    continue
                count = self.schedule.count_sum_reservation(name, start)
                if count > 1:
                    print("You have reached the maximum number of reservations (2) for this week.")

                start_date = self.schedule.check_if_court_is_reserved_start_date(start)
                if start_date.hour >= 22 or start_date.hour < 8:
                    print("Courts are open from 8 to 22, or there are no free dates available.")
                    continue
                if start != start_date:
                    while True:
                        answer = input(
                            f'The time you chose is unavailable, would you like to make a reservation'
                            f' for {start_date.strftime("%d.%m.%Y %H:%M")} instead? (Y/N)\n')
                        if answer == "Y":
                            break
                        elif answer == "N":
                            start_date = None
                            break
                        else:
                            print("Invalid action. Please try again.\n")
                if start_date:
                    break
            except ValueError:
                print("Incorrect date format. Please try again.\n")

        if start_date.hour == 21 and start_date.minute == 30:
            while True:
                duration = input("How long would you like to book court?\n1) 30 Minutes\n")
                if duration == "1":
                    end_date = start_date + datetime.timedelta(minutes=30)
                    if self.schedule.check_if_court_is_reserved_end_date(end_date) == False:
                        print("No free date\n")
                        continue
                    break
                else:
                    print("Wrong choise. Please try again.\n")
        elif start_date.hour >= 17 and start_date.hour <= 21:
            while True:
                duration = input("How long would you like to book court?\n1) 30 Minutes\n2) 60 Minutes\n")
                if duration == "1":
                    end_date = start_date + datetime.timedelta(minutes=30)
                    if self.schedule.check_if_court_is_reserved_end_date(end_date) == False:
                        print("No free date\n")
                        continue
                    break
                elif duration == "2":
                    end_date = start_date + datetime.timedelta(minutes=60)
                    if self.schedule.check_if_court_is_reserved_end_date(end_date) == False:
                        print("No free date\n")
                        continue
                    break

                else:
                    print("Wrong choise. Please try again.\n")
        else:
            while True:
                duration = input(
                    "How long would you like to book court?\n1) 30 Minutes\n2) 60 Minutes\n3) 90 Minutes\n")
                if duration == "1":
                    end_date = start_date + datetime.timedelta(minutes=30)
                    if self.schedule.check_if_court_is_reserved_end_date(end_date) == False:
                        print("No free date\n")
                        continue
                    break
                elif duration == "2":
                    end_date = start_date + datetime.timedelta(minutes=60)
                    if self.schedule.check_if_court_is_reserved_end_date(end_date) == False:
                        print("No free date\n")
                        continue
                    break
                elif duration == "3":
                    end_date = start_date + datetime.timedelta(minutes=90)
                    if self.schedule.check_if_court_is_reserved_end_date(end_date) == False:
                        print("No free date\n")
                        continue
                    break
                else:
                    print("Wrong choise. Please try again.\n")

        reservation = Reservation(name, start_date, end_date)
        return self.schedule.add(reservation)

    def cancel_reservation(self):
        self.schedule.cancel_reservation()

    def print_schedule(self):
        self.schedule.show()

    def save_schedule(self):
        self.schedule.save_schedule()

    def main(self):
        self.run()


# if __name__ == "__main__":
#     system = TennisReservationSystem()
#     system.main()