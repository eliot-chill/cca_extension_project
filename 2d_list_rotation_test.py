region = [[1,2,3],[4,5,6],[7,8,9]]

def print_array(array):
    for j in range(len(array)):
        for i in range(len(array)):
            if i != 3:
                print(array[j][i], end = ' ')
            else:
                print(array[j][i])
        print("\n")



def transpose_array(array):
    temp_array = list(map(list, zip(*array)))
    return temp_array



def switch_array_columns(array):
    temp_first_col = array[0]
    temp_last_col = array[len(array)-1]

    first_col = temp_last_col
    last_col = temp_first_col

    array[0] = first_col
    array[len(array)-1] = last_col

    return array

def rotate_array_anti_clockwise(array):
    array = transpose_array(array)
    array = switch_array_columns(array)

    return array

def rotate_array_clockwise(array):
    array = switch_array_columns(array)
    array = transpose_array(array)

    return array


#print_array(region)
print_array(region)
region = rotate_array_clockwise(region)

print_array(region)
