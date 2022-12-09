def get_str():
    str1 = input("Enter a word: ")
    return str1


def reverse(str1):
    for i in (str1.split()[::-1]):
        print(i, end=" ")


data = get_str()
reverse(data)
