"""A module for rotating the various regions of the board. This is
accomplished through ideas surrounding matrices."""

#To transpose a region is to make the columns, rows, and the rows, columns.
def transpose_region(region):
    #This is done simply using one line
    temp_region = list(map(list, zip(*region)))

    return temp_region
#This switches the first and last columns of the region.
def switch_region_columns(region):

    temp_first_col = region[0]
    temp_last_col = region[len(region)-1]

    first_col = temp_last_col
    last_col = temp_first_col

    region[0] = first_col
    region[len(region)-1] = last_col

    return region

#rotating it clockwise one step consists of:
#1.switching the position of the first and last columns and,
#2.transposing the matrix
def rotate_region_clockwise(region):

    region = switch_region_columns(region)

    region = transpose_region(region)

    return region

#rotating it anticlockwise one step consists of:
#1.transposing the matrix and,
#2.switching the position of the first and last columns
def rotate_region_anticlockwise(region):

    region = transpose_region(region)

    region = switch_region_columns(region)

    return region
