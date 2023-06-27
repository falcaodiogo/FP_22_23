# This function checks if year is a leap year.
# It is wrong: 1900 was a common year!
def isLeapYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return year%4 == 0

# This function has a semantic error: February in a leap year should return 29!
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

# This is wrong, too.
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
    assert (month > 0) and (day > 0) and (year > 0)
    if month <= 12:
       if isLeapYear(year) == True:    #28 se LeapYear e 29 de não LeapYear
            if day == 29:
                return True
            else:
                return False
       elif isLeapYear(year) == False:
            if day == 28:
                return True
            else:
                return False
    else:
        return False
    
# This is the main function
def main():
    print("Was", 2017, "a leap year?", isLeapYear(2017))    # False?
    print("Was", 2016, "a leap year?", isLeapYear(2016))    # True?
    print("Was", 2000, "a leap year?", isLeapYear(2000))    # True?
    print("Was", 1900, "a leap year?", isLeapYear(1900))    # False?
    
    print("January 2017 had", monthDays(2017, 1), "days")   # 31?
    print("February 2017 had", monthDays(2017, 2), "days")  # 28?
    print("February 2016 had", monthDays(2016, 2), "days")  # 29?
    print("February 2000 had", monthDays(2000, 2), "days")  # 29?
    print("February 1900 had", monthDays(1900, 2), "days")  # 28?
    
    y, m, d = nextDay(2017, 1, 30)
    print(y, m, d)    # 2017 1 31 ?
    y, m, d = nextDay(2017, 1, 31)
    print(y, m, d)    # 2017 2 1 ?
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)    # 2017 3 1 ?
    y, m, d = nextDay(2016, 2, 29)
    print(y, m, d)    # 2016 3 1 ?
    y, m, d = nextDay(2017, 12, 31)
    print(y, m, d)    # 2018 1 1 ?

# call the main function
main()