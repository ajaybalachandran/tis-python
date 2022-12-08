list1 = input('Enter the elements of list: ').split()
num_list = list(map(int, list1))
sum1 = 0
for i in num_list:
    sum1 += i
avg1 = sum1 / len(num_list)
print(f'sum = {sum1}, average = {avg1}')