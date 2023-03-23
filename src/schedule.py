import csv
import json
import datetime


class Schedule:
    def __init__(self):
        self.list_of_reservations = []

    def add(self, reservation):
        self.list_of_reservations.append(reservation)

    def show(self):
        sorted_reservations = sorted(
            self.list_of_reservations, key=lambda r: r.start_date
        )
        if not self.list_of_reservations:
            print("No reservations")
            return
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        for reservation in sorted_reservations:
            if reservation.start_date.date() == today:
                print("Today:")
            elif reservation.start_date.date() == tomorrow:
                print("Tomorrow:")
            else:
                print(reservation.start_date.strftime("%A") + ":")
            reservation.display()

    def count_sum_reservation(self, name: int, start_date: int):
        count = 0
        week = start_date.isocalendar()[1]
        year = start_date.year
        for reservation in self.list_of_reservations:
            if (
                reservation.name == name
                and reservation.number_of_week == week
                and reservation.start_date.year == year
            ):
                count += 1
        return count

    def check_if_court_is_reserved_start_date(self, start_date: int):
        sorted_reservations = sorted(
            self.list_of_reservations, key=lambda r: r.start_date
        )
        if len(sorted_reservations) == 1:
            if (
                sorted_reservations[0].start_date
                <= start_date
                < sorted_reservations[0].end_date
            ):
                return sorted_reservations[0].end_date
            else:
                return start_date
        i = 0

        while i < len(sorted_reservations):
            if (
                sorted_reservations[i].start_date
                <= start_date
                < sorted_reservations[i].end_date
                and sorted_reservations[i].end_date + datetime.timedelta(minutes=30)
                > sorted_reservations[i + 1].start_date
            ):
                start_date = sorted_reservations[i + 1].end_date
                i += 1
                continue
            if (
                sorted_reservations[i].start_date
                <= start_date
                < sorted_reservations[i].end_date
            ):
                return sorted_reservations[i].end_date
            i += 1
        return start_date

    def check_if_court_is_reserved_end_date(self, end_date: str):
        for reservation in self.list_of_reservations:
            if reservation.start_date < end_date <= reservation.end_date:
                return False

        return True

    def cancel_reservation(self):
        name = input("Enter your name: ")
        while True:
            date_str = input("Enter reservation date and time: {DD.MM.YYYY HH:MM}: ")
            try:
                start_date = datetime.datetime.strptime(date_str, "%d.%m.%Y %H:%M")
                break
            except ValueError:
                print("Incorrect date format. Please try again.\n")

        for reservation in self.list_of_reservations:
            if (
                reservation.name == name
                and reservation.start_date == start_date
                and start_date - datetime.timedelta(minutes=60)
                > datetime.datetime.now()
            ):
                self.list_of_reservations.remove(reservation)
                return print("Reservation canceled.\n")
            elif reservation.name == name and reservation.start_date != start_date:
                return print("No reservations for this user.\n")
            elif (
                reservation.name == name
                and reservation.start_date == start_date
                and start_date - datetime.timedelta(minutes=60)
                < datetime.datetime.now()
            ):
                return print(
                    "Reservations cannot be canceled less than 1 hour before the start.\n"
                )
        print("Reservation not found.\n")

    def save_to_file_csv(self, filename: str, start_date: str, end_date: str):
        sorted_reservations = sorted(
            self.list_of_reservations, key=lambda r: r.start_date
        )
        filename = f"{filename}.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Start Date", "End Date"])
            for reservation in sorted_reservations:
                if (
                    reservation.start_date >= start_date
                    and reservation.end_date <= end_date
                ):
                    writer.writerow(
                        [reservation.name, reservation.start_date, reservation.end_date]
                    )
            print(f"Schedule saved to {filename} in CSV format\n")

    def save_to_file_json(self, filename: str, start_date: str, end_date: str):
        sorted_reservations = sorted(
            self.list_of_reservations, key=lambda r: r.start_date
        )
        filename = f"{filename}.json"
        reservations_json = []
        for reservation in sorted_reservations:
            if (
                reservation.start_date >= start_date
                and reservation.end_date <= end_date
            ):
                reservation_dict = {
                    "name": reservation.name,
                    "start_date": reservation.start_date.isoformat(),
                    "end_date": reservation.end_date.isoformat(),
                }
                reservations_json.append(reservation_dict)
        with open(filename, "w") as file:
            json.dump(reservations_json, file, indent=2)
        print(f"Schedule saved to {filename} in JSON format\n")

    def save_schedule(self):
        start = input("Enter the reservation start date in the format DD.MM.YYYY: ")
        end = input("Enter the reservation end date in the format DD.MM.YYYY: ")
        file_format = input("Enter the file format (csv or json): ")
        filename = input("Enter the file name: ")
        start_date = datetime.datetime.strptime(start, "%d.%m.%Y")
        end_date = datetime.datetime.strptime(end, "%d.%m.%Y")

        if file_format == "csv":
            return self.save_to_file_csv(filename, start_date, end_date)

        elif file_format == "json":
            return self.save_to_file_json(filename, start_date, end_date)
        else:
            print("Invalid file format. Please enter 'csv' or 'json'.")
