month = int(input('Enter the month as a number '))
year = int(input('Enter year as a number '))
Days = 0
if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
    Days = 31
elif month == (4 or 6 or 9 or 11):
    Days = 30
elif month == 2 and (year % 4 != 0):
    Days = 28
elif month == 2 and (year % 4 == 0):
    Days = 29  # it is a leap year
else:
    print('Invalid month number')
print(Days)
