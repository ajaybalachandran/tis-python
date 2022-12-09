list1 = list(map(int, input('Enter the elements of list: ').split()))
for i in list1:
    while i % 5 == 0:
        if (i > 150) and (i < 500) and (i % 5 == 0):
            break
        elif i > 500:
            continue
        print(i, end=' ')
        break
