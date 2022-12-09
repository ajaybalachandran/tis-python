# 10. Write a function which counts the number of occurrences of item 10 from a tuple and prints the
# output. Eg tuple : tuple1 = (20, 10, 35, 10, 34, 50, 10)

def count_occurrence():
    tuple1 = tuple(list(map(int, input('Enter the elements: ').split())))
    cnt = 0
    for i in tuple1:
        if i == 10:
            cnt += 1
    print(f'The number of occurrence of element 10 is: {cnt}')

count_occurrence()