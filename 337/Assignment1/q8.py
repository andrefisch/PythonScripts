'''
leapYear - determines if the given year is a leap year using the
provided forumla
'''
def leapYear(year):
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


'''
convertDay - if we are in january it doesn't matter whether it is a leap year
or not. if it is not in january, and if it is a leap year, subtract one from
the given day number. then subtract a number of days equal to all of the days
of all of the preceeding months added up to get the day number of this month
'''
def convertDay(year, day):
    monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # January
    if day <= 31:
        return " ".join([monthNames[0], str(day), ",", str(year)])

    if leapYear(year):
        day = day - 1

    # February
    if day <= 59:
        return " ".join([monthNames[1], str(day - 31), ",", str(year)])
    # March
    elif day <= 90:
        return " ".join([monthNames[2], str(day - 59), ",", str(year)])
    # April
    elif day <= 120:
        return " ".join([monthNames[3], str(day - 90), ",", str(year)])
    # May
    elif day <= 151:
        return " ".join([monthNames[4], str(day - 120), ",", str(year)])
    # June
    elif day <= 181:
        return " ".join([monthNames[5], str(day - 151), ",", str(year)])
    # July
    elif day <= 212:
        return " ".join([monthNames[6], str(day - 181), ",", str(year)])
    # August
    elif day <= 243:
        return " ".join([monthNames[7], str(day - 212), ",", str(year)])
    # September
    elif day <= 273:
        return " ".join([monthNames[8], str(day - 243), ",", str(year)])
    # October
    elif day <= 304:
        return " ".join([monthNames[9], str(day - 273), ",", str(year)])
    # November
    elif day <= 334:
        return " ".join([monthNames[10], str(day - 304), ",", str(year)])
    # December
    elif day <= 365:
        return " ".join([monthNames[11], str(day - 334), ",", str(year)])

def main():
    dates = [0, 0]
    while dates[0] != -1:
        date = raw_input("Enter a year and a day number separated by a comma: ")
        dates = date.split(",")
        dates[0] = int(dates[0])
        dates[1] = int(dates[1])
        if dates[0] != -1:
            print convertDay(dates[0], dates[1])

main()
