from datetime import timedelta, date
import uuid

class Reservation:

  def __init__(self, date, customer_info):
    self.date = date
    self.customer_info = customer_info

  def get_date(self):
    return self.date

  def get_customer_info(self):
    return self.customer_info
