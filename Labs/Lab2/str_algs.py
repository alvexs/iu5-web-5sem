def turn_string(string_):
    temp_string = ''
    for x in range(0, len(string_)):
        temp_string += string_[-x - 1]
    print(temp_string)


test_string = input('Введите строку\n')
turn_string(test_string)
