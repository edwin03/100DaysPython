def is_leap_year(year):
  """This will return a boolean answer if the year is leap year.
  This is a very cool tool"""
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

is_leap_year()