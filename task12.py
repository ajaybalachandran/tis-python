# 12. Write a program to subtract a week (7 days) from a given date in Python and print the output.
import datetime
print('Enter date in dd mm yy format!!!!')
date1 = list(map(int, input('Enter the date: ').split()))
d1 = datetime.datetime(date1[2], date1[1], date1[0])
ans = d1.date()-datetime.timedelta(days=7)
print(f'{ans.day}-{ans.month}-{ans.year}')