def arr_min(array_):
    temp_array = array_
    min = temp_array[0]
    for x in temp_array:
        if x < min:
            min = x
    print(min)


def arr_average(array_):
    temp_array = array_
    avg = 0
    for x in temp_array:
        avg += x
    avg /= 2
    print(avg)


test_array = []
print("Введите сначала число элементов, а затем элементы массива")
for i in range(int(input())):
    test_array.append(int(input()))
arr_min(test_array)
arr_average(test_array)
