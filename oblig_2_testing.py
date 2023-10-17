from oblig_2 import isLeapYear

# True means its a leap year
# False means its not a leap year

#To be a leap year, the year number must be divisible by four – except for end-of-century years,
# which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.

def test_is_divisible_by_100_but_not_400():
    # 2000 is divisible by 100 and 400 so we should get True
    assert isLeapYear(2000) == True

def test_not_divisible_by_100_but_not_400():
    # 1900 is divisible by 100 but not 400 so we should get False return
    assert isLeapYear(1900) == False

def test_year_is_a_leap_year_when_divisible_by_4():
    # 1936 is divisible by 4 and should therefore return True
    assert isLeapYear(1936) == True

def test_year_is_not_a_leap_year_when_divisible_by_4():
    # 1801 is not divisible by 4 and should return False
    assert isLeapYear(1801) == False

def test_year_is_divisible_by_4_but_not_100():
    # 1804 is divisible by 4 but not 100 and should return True
    assert isLeapYear(1804) == True
    