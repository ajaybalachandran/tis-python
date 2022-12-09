from random import randint
# method 1
# rand_list = [randint(33, 126) for x in range(10)]
# print('Secret Code is: ', end=' ')
# for i in list(map(chr, rand_list)):
#     print(i, end='')
# print()

# method 2

print(f'Secret code is: {"".join(map(chr, [randint(33, 126) for x in range(10)]))}')
