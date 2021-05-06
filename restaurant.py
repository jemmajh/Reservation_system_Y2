import datetime
import table
import restaurant

class Restaurant:
  def __init__(self):
    self.tables = []
    self.name = "Restaurant Dingo"
    for i in range(8):
      self.tables.append(table.Table(i))

  def get_tables(self):
    return self.tables

  def print_tables(self):
    for i in range(8):
      print("Table " + str(i))
      
def loop_opening_hours(action):
  dt = datetime.datetime.now()
  newdate = dt.replace(hour=12, minute=0)
  for i in range(12, 20):
    newdate = dt.replace(hour=i, minute=0)
    action(newdate)