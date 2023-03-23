import datetime

from src.reservation import Reservation
from src.schedule import Schedule


def test_should_add_reservation():
    schedule = Schedule()
    start = datetime.datetime.strptime("10.10.2023 10:00", "%d.%m.%Y %H:%M")
    end = datetime.datetime.strptime("10.10.2023 11:00", "%d.%m.%Y %H:%M")
    reservation = Reservation("Customer", start, end)
    schedule.add(reservation)
    assert len(schedule.list_of_reservations) == 1
    assert schedule.list_of_reservations[0] == reservation


def test_should_count_sum_reservation():
    schedule = Schedule()
    start = datetime.datetime.strptime("10.10.2023 10:00", "%d.%m.%Y %H:%M")
    end = datetime.datetime.strptime("10.10.2023 11:00", "%d.%m.%Y %H:%M")
    reservation = Reservation("Customer", start, end)
    schedule.add(reservation)

    assert schedule.count_sum_reservation("Customer", start) == 1


def test_should_delete_reservation():
    schedule = Schedule()
    start = datetime.datetime.strptime("10.10.2023 10:00", "%d.%m.%Y %H:%M")
    end = datetime.datetime.strptime("10.10.2023 11:00", "%d.%m.%Y %H:%M")
    reservation = Reservation("Customer", start, end)
    schedule.add(reservation)
    schedule.list_of_reservations.remove(reservation)
    assert len(schedule.list_of_reservations) == 0
