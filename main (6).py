# leap year
"""
year/4==0 &
year/100!=0 |
year/400==0
"""


def isleapyear(year):
  if (year / 4 == 0 and year / 100 != 0) or year / 400 == 0:
    return True
  else:
    return False


year = 2024

if isleapyear(year):
  print("2024 is a leap year")
else:
  print("2024 is not a leap year")
