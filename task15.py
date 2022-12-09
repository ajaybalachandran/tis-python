# 15. Create a program that asks the user for a number and then print the list of all the divisors of that
# number. (If you don’t know what a divisor is, it is a number that divides evenly into another
# number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num1 = int(input('Enter a number: '))
divisors_list = []
for i in range(1, num1+1):
    if num1 % i == 0:
        divisors_list.append(i)
print(f'Divisors of {num1} are: {divisors_list}')
