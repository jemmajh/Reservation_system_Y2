from datetime import timedelta, date
import reservation

class Table:

  def __init__(self, number):
    self.number = number
    self.reservations = []

  
  def get_number(self):
    return self.number

  def get_reservations(self):
    return self.reservations

  def get_reservations_for_day(self, target_date):
    reservations = []
    for res in self.reservations:
      date = res.get_date()
      #print(str(date.year) + " " + str(date.month) + " " + str(date.day))
      #print(str(target_date.year) + " " + str(target_date.month) + " " + str(target_date.day))
      if (date.year == target_date.year and date.month == target_date.month and date.day == target_date.day):
        reservations.append(res)
    return reservations

  def add_reservation(self, target_date, identifier):
    reservation1 = reservation.Reservation(target_date, identifier)
    self.reservations.append(reservation1)

  def remove_reservation(self, target_reservation):
    for r in self.reservations:
      if (r.get_date().date() == target_reservation.get_date().date() and r.get_customer_info() == target_reservation.get_customer_info()):
        self.reservations.remove(r)
        break
