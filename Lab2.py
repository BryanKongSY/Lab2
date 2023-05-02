def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5, 67, 32)")

def get_user_input():
    print('Enter values:')
    x = input()
    y = x.split(", ")
    temp = []
    for item in y:
        temp.append(float(item))
    return temp

def calc_average_temperature(y):
    avg = sum(y) / len(y)
    print(avg)
    return avg

def calc_min_max_temperature(z):
    minimum = min(z)
    maximum = max(z)
    print(maximum, minimum)
    return minimum, maximum

display_main_menu()
global temp
temp = get_user_input()
calc_average_temperature(temp)
calc_min_max_temperature(temp)