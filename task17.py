def get_age():
    return int(input('Enter your age: '))


def get_gender():
    return input(f'Enter your gender (M / F): ')


def marital_status():
    return input('Are you Married (Y / N): ')


ctrl = "y"
while ctrl == 'y':
    age = get_age()
    gender = get_gender()
    status = marital_status()
    if gender == 'f':
        print('You can work only in urban areas')
    elif gender == 'm' and (20 <= age < 40):
        print('You can work Anywhere')
    elif gender == 'm' and (40 <= age <= 60):
        print('You can work only in urban areas')
    else:
        print('ERROR!!!!!')
    print('=====================================================')
    ctrl = input('Do you want to continue(Y / N): ')
    print('=====================================================')
