def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  """This function calculate the number of days in a month, 
  moreover utilizes the is_leap function to verificate if is a leap year or not"""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  leap_verification = is_leap(year)
  if leap_verification:
    month_days[1] = 29
  return month_days[month - 1]

year = int(input("Insert the year: "))
month = int(input("Insert the month: ")) 
days = days_in_month(year, month)
print(days)

