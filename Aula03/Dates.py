
# Function isLeapYear(year) should return True if year is a leap year
# and False otherwise.  Fix it.
# (See: https://en.wikipedia.org/wiki/Leap_year)
def isLeapYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return year%4 == 0


# monthDays should return the number of days in a given month and year.
# For exemple, February in a leap year should return 29.
# Correct it.
def monthDays(year, month):
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        # This tuple contains the days in each month (on a common year).
        # For example: MONTHDAYS[3] is the number of days in March.
        days = MONTHDAYS[month]
        return days


# nextDay should return the day after the given date.
# For example: nextDay(2017, 1, 31) should return (2017, 2, 1)
def nextDay(year, month, day):
    if day < monthDays(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1



# Define a function dateIsValid that
# returns the boolean True if the given arguments form a valid date and
# returns False if not.
# For example: dateIsValid(1980, 2, 29) should return True,
# dateIsValid(1980, 2, 30) should return False.
def dateIsValid(year, month, day):
    if (month <=0 or year<=0 or day<=0):
    	return False
    elif month <= 12:
          if day == monthDays(year, month):
             return True
          else:
             return False
    else:
    	return False
    

# Define a function previousDay that returns the day before the given date.
# For example: previousDay(1980, 3, 1) should return (1980, 2, 29)
def previousDay(year, month, day):
   if monthDays(year, month)-day > 0: 
        if (day-1) == 0:
            return year, month-1 , monthDays(year, month-1)
        else:
            return year, month, day - 1
   else:
        if month == 1:
            return year - 1, 12, 31
        else:
            return year, month - 1, day -1


# DO NOT CALL any function!  Codecheck will do that automatically.
