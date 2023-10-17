def isLeapYear(year):
    if year <= 1582:
        print("Year must be after 1582")

    # Year is divisible by 100 and 400
    if year % 100 == 0 and year % 400 == 0:
        return True

    # Year is divisible by 4 and not 100
    elif year % 4 == 0 and year % 100 != 0:
        return True

    else:
        return False


