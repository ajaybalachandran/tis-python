list1 = input('Enter the elements of list: ').split()
key = input('Enter the element to search: ')
print(f'list before deleting element: {list1}')
for i in list1:
    if i == key:
        list1.remove(i)
print(f'list after deleting element: {list1}')


