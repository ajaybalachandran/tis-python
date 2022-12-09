def my_count_fun():
    f0 = open('file.txt', 'a')
    f0.close()
    f1 = open('file.txt', 'r')
    list1 = list(f1.read())
    f1.seek(0)
    alphabets = 0
    blank_space = 0
    lower_case = 0
    word = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in list1:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            alphabets += 1
        if ord(i) == 32:
            blank_space += 1
        if 97 <= ord(i) <= 122:
            lower_case += 1
    for line in f1:
        for j in line.split():
            if j[0] in vowels:
                word += 1
    f1.close()
    print(f'Number of alphabets = {alphabets}')
    print(f'Number of blank spaces = {blank_space}')
    print(f'Number of lowercase letters = {lower_case}')
    print(f'Number of words starts with vowel = {word}')


my_count_fun()
