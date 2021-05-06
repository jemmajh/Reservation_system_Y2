import restaurant
import os 
import datetime
import json
import pickle 

def get_restaurant_from_file():
  fileptr = open(os.getcwd() + "//restaurant_file", 'rb')
  try:
    data = pickle.load(fileptr)
    return data
  except EOFError:
    return None
    

def save_restaurant_to_file(data):
  with open(os.getcwd() + "//restaurant_file", 'wb') as fil:
    pickle.dump(data, fil)


def main():

  #attempt to load from file. If fails, just create new restaurant object
  restaurant_attempt = get_restaurant_from_file()
  if (restaurant_attempt == None): restaurant1 = restaurant.Restaurant()
  else: restaurant1 = restaurant_attempt

  while (True):
    print("\nWelcome to restaurant Dingo! How may we help you today?")
    print("1: Check tables")
    print("2: Reserve a table")
    print("3: Cancel reservation")
    print("4: List reservations")
    print("5: END\n")
    chosen = input("Choose option (enter a number 1-3): ")

    #CHECK TABLE SITUATION
    if (chosen == "1"):
      table_number, target_day, target_hour = get_params_from_user(False, "Enter the day you want to check, in format DD.MM.YYYY: ", False)
      if (target_day == None): continue
      print("\nTABLES SITUATION ON " + target_day.strftime("%d.%m.%Y") + "\n")
      print("{:<9}".format("Table #"),  end='')  
      def header_action(iterated_hour):
        print("{:>8}".format(iterated_hour.strftime("%H:00")),  end='')
      restaurant.loop_opening_hours(header_action)
      print("\n")

      tables = restaurant1.get_tables()
      for i in range(8):
        table = tables[i]
        reservations = table.get_reservations_for_day(target_day)
        print("{:<9}".format("Table " + str(i + 1)), end='')

        def row_action(iterated_hour):
          reserved = False
          for reservation in reservations:
            res_date = reservation.get_date()
            if (res_date.hour == iterated_hour.hour):
              reserved = True
              break
          if (reserved): print("{:>8}".format("X"),  end='')
          else: print("{:>8}".format("FREE"),  end='')

        restaurant.loop_opening_hours(row_action)
        print("\n")

    #RESERVE TABLES
    elif (chosen == "2"):
      table_number, target_day, date_hour = get_params_from_user("Enter the number of the table you want to reserve (1-8): ", "Enter the day you want to reserve, in format DD.MM.YYYY: ", "Enter the hour you want to reserve (12-19), in format HH: ")
      if (table_number == None or target_day == None or date_hour == None): continue
      table = restaurant1.get_tables()[table_number - 1]
      reservations = table.get_reservations_for_day(target_day)
      reserved = False
      for reservation in reservations:
        if (reservation.get_date().hour == int(date_hour.hour)):
          reserved = True
          break
      if (reserved):
        print("\nThis hour has already been reserved. Check the tables for availability.\n")
      else:
        info = input("Enter your name to create a unique reservation: ")
        table.add_reservation(date_hour, info)
        print("\nA reservation was successfully created for " + info + " in " + date_hour.strftime("%d.%m.%Y at %H:00") + "\n")
      
    #CANCEL RESERVATIONS
    elif (chosen == "3"):
      table_number, target_day, date_hour = get_params_from_user("Enter the number of the table you want to cancel (1-8): ", "Enter the day you want to cancel, in format DD.MM.YYYY: ", "Enter the hour you want to cancel (12-19), in format HH: ")
      if (table_number == None or target_day == None or date_hour == None): continue
      table = restaurant1.get_tables()[table_number - 1]
      reservations = table.get_reservations_for_day(target_day)
      target_reservation = None
      for reservation in reservations:
        if (reservation.get_date().hour == int(date_hour.hour)):
          target_reservation = reservation
          break
      if (target_reservation == None):
        print("\nThis time is not reserved.\n")
      else:
        name = input("Enter your name to confirm it's you: ")
        if (name != target_reservation.get_customer_info()):
          print("\nThis name is not the same as the reservation. Cancelation cannot be done.\n")
        else:
          table.remove_reservation(target_reservation)
          print("\nThe reservation was successfully removed.\n")

    elif (chosen == "4"):
      table_number, target_day, date_hour = get_params_from_user(False, "Enter the day you want to list, in format DD.MM.YYYY: ", False)
      if (target_day == None): continue
      tables = restaurant1.get_tables()
      for table in tables:
        reservations = table.get_reservations_for_day(target_day)
        for reservation in reservations:
          print("Table " + str(table.get_number()) + " - " + str(reservation.get_date().strftime("%d.%m.%Y %H:00")))

    elif (chosen == "5"):
      save_restaurant_to_file(restaurant1)
      break

    else:
      print("\nThere is no option with input " + chosen + ". Please try again.\n")



def get_params_from_user(table_number_prompt, date_prompt, hour_prompt):
  table_number = None
  date = None
  hour = None
  if (table_number_prompt != False):
    try:
      table_number = int(input(table_number_prompt))
      if table_number < 1 or table_number > 8: raise ValueError
    except ValueError:
      print("\nERROR: The table number must be a number between 1 and 8.\n")
      return None, None, None
  
  if (date_prompt != False):
    date_string = input(date_prompt)
    arr = date_string.split(".")
    try:
      if len(arr) != 3: raise ValueError
      date = datetime.datetime(int(arr[2]),int(arr[1]), int(arr[0]))
    except ValueError:
      print("\nERROR: date could not be read. Next time please enter the target date in format DD.MM.YYYY!\n")
      return None, None, None

  if (hour_prompt != False):
    hour_string = input(hour_prompt)
    try:
      hour = datetime.datetime(int(arr[2]),int(arr[1]), int(arr[0]), int(hour_string))
      if int(hour_string) < 12 or int(hour_string) > 19: raise ValueError()
    except ValueError:
      print("\nERROR: hour could not be read. Next time please enter the target hour (12-19) in format HH!\n")
      return None, None, None

  return table_number, date, hour


main()


