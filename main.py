def replace(array):
    for i in range(len(array)):
        if array[i] == "Null":
            array[i] = 0
    return array


print(replace([1, 2, "Null", 3, 4]))
