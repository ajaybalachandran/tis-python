# Sort a list of integers in Descending order( without using built-in sorted function )

list1 = list(map(int, input('Enter the elements of list: ').split()))
list2 = []
while list1:
    key = list1[0]
    for i in list1:
        if i > key:
            key = i
    list2.append(key)
    list1.remove(key)

print(list2)