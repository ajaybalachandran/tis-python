import datetime
def date_diff():
    print('Enter date in dd mm yy format!!!!')
    date1 = list(map(int, input('Enter the date1: ').split()))
    date2 = list(map(int, input('Enter the date2: ').split()))
    d1 = datetime.datetime(date1[2], date1[1], date1[0])
    d2 = datetime.datetime(date2[2], date2[1], date2[0])
    ans = abs(d1.date() - d2.date())

    if ans:
        print(f'{ans.days} days')
    else:
        print('0 days')
date_diff()