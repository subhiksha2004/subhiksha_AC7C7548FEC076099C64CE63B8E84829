#leap year
def isleap year (year):
 if (year %4==0 and year % 100!=0) or year % 400==0:
 return True
else:
  return False

year=2013

if iisleapyear(year):
 print('{} is a leap year.'.format(year))
else:
  printprint('{}is not a leap year.'.formate(year))

