def transpose_region(region):

    temp_region = list(map(list, zip(*region)))

    return temp_region

def switch_region_columns(region):

    temp_first_col = region[0]
    temp_last_col = region[len(region)-1]

    first_col = temp_last_col
    last_col = temp_first_col

    region[0] = first_col
    region[len(region)-1] = last_col

    return region


def rotate_region_clockwise(region):

    region = switch_region_columns(region)

    region = transpose_region(region)

    return region

def rotate_region_anticlockwise(region):

    region = transpose_region(region)

    region = switch_region_columns(region)

    return region
