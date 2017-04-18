# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!

#daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False



def daysInMonth(year, month):   # NEED TO CALL THIS ONE.
    # if month in (1, 3, 5, 7, 8, 10, 12)
    if month == 1 or month ==3 or month == 5 or month == 7 \
       or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30




def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    day += 1
    if day > 30:
        day = 1
        month += 1
    if month > 12:
        month = 1
        year += 1
    return  year, month, day




def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
        year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False





def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    days = 0
    month1 = daysInMonth(year1, month1)
    month2 = daysInMonth(year2, month2)
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days







def mytest():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"









def test():
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    #assert nextDay(2013, 1, 1) == (2013, 1, 2)
    #assert nextDay(2013, 4, 30) == (2013, 5, 1)
    #assert nextDay(2012, 12, 31) == (2013, 1, 1)
    #assert nextDay(2013, 2, 28) == (2013, 3, 1)
    #assert nextDay(2013, 9, 30) == (2013, 10, 1)

    #assert nextDay(2012, 2, 28) == (2012, 2, 29)
    #assert daysBetweenDates(2012, 1, 1, 2013, 1, 1) == 366
    #assert daysBetweenDates(2013, 1, 1, 2014, 1, 1) == 365
    #assert daysBetweenDates(2013, 1, 24, 2013, 6, 29) == 156
    days = daysBetweenDates(2013, 1, 1, 2013, 1, 1)
    print "This many days have passed: " + str(days)
    days = daysBetweenDates(2013, 1, 1, 2013, 1, 2)
    print "This many days have passed: " + str(days)
    days = daysBetweenDates(1988, 1, 11, 2017, 4, 12)
    print "This many days have passed: " + str(days)
    print "Test Finished!"

test()









# Some of these tests failed.
# Need to review this.
