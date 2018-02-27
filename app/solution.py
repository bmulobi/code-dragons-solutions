import math
import numpy as np

import modes

pizza = []
lines = None

def get_slice_shape(factor1, factor2, fits):
    slice_rows = factor1 if fits else factor2
    slice_cols = factor2 if fits else factor1

    return (slice_rows, slice_cols)

def get_file_contents(filename):
    with open(filename) as file:
        lines = file.read().strip().split('\n')
    return lines


def get_start_indices(start_point, rows, cols):
    if start_point == "TL":
        start_row = 0
        start_col = 0
    elif start_point == "TR":
        start_row = 0
        start_col = cols - 1
    elif start_point == "BL":
        start_row = rows - 1
        start_col = 0
    else:
        start_row = rows - 1
        start_col = cols - 1

    return (start_row, start_col)

def tl_horizontal_right(shapes, rows, cols, pizza, min, max):
    for shape in shapes:
        # cut from top left horizontally
        slices = []
        num_rows = int(shape[0])
        num_cols = int(shape[1])
        start_row = 0
        end_row = num_rows

        horizontal_steps = int(math.floor(cols / num_cols))
        vertical_steps = int(math.floor(rows / num_rows))

        for v_step in range(0, vertical_steps):
            start_col = 0
            end_col = num_cols

            invalid_slice = False

            for h_step in range(0, horizontal_steps):
                slice = pizza[start_row:end_row, start_col:end_col]
                print(slice)

                unique, counts = np.unique(slice, return_counts=True)

                if len(unique) < 2 or (counts[0] < min or counts[1] < min):
                    invalid_slice = True
                    break
                else:
                    slices.append((start_row, start_col, end_row - 1, end_col - 1))

                if h_step < horizontal_steps - 1:
                    start_col = end_col
                    end_col += num_cols

            if invalid_slice:
                slices.clear()
                break
            else:
                if v_step < vertical_steps - 1:
                    start_row = end_row
                    end_row += num_rows

        # test remaining cells for slice validity
        if end_col < cols:
            # try with slices of size range min * 2 to max + 1

            for size in range(min * 2, max + 1):
                if rows % size == 0:
                    for vstep in range(int(math.ceil(rows / size))):

                else:
                    continue





            print("cols unsuccess - ", shape, end_col)

        if end_row < rows:
            untouched_rows = rows - end_row


            print("rows unsuccess - ", shape, end_row)

        if end_row == rows and end_col == cols:
            print("Success ", shape, slices)
            break

lines = get_file_contents("example.in")

if lines:
    for index in range(len(lines)):
        if index == 0:
            header = [int(x) for x in lines[index].split()]

            rows = header[0] # total pizza rows
            cols = header[1] # total pizza cols
            min = header[2] # min cells per ingredient
            max = header[3] # max cells per slice

            max_slices = rows * cols / max

            if isinstance(max_slices, float):
                max_slices = math.ceil(max_slices) if int(str(max_slices).split('.')[1])\
                                                      >= min * 2 else math.floor(max_slices)
        else:
            pizza.append([x for x in lines[index]])

    del lines
    pizza = np.array(pizza)

    # infer possible shapes of majority of the slices from max and pizza dimensions
    shapes = []
    if max in [2,3,5,7]:
        fits = max <= rows
        shapes.append(get_slice_shape(max, 1, fits))
    else:
        for num in range(2,10):
            if num == max:
                break
            if max % num == 0:
                quotient = max / num
                fits = quotient <= rows

                shapes.append(get_slice_shape(quotient, num, fits))

    print(shapes)
    # exit(0)
    # use various shapes to attempt for max_slices (the goal)
    tl_horizontal_right(shapes, rows, cols, pizza, min, max)










            # cut from top right horizontally

            # cut from bottom left horizontally

            # cut from bottom right horizontally

            # cut from top left vertically

            # cut from top right vertically

            # cut from bottom left vertically

            # cut from bottom right vertically

    # [6, 7, 1, 5]
    '''
    6 7 1 5
    TMMMTTT
    MMMMTMM
    TTMTTMT
    TMMTMMM
    TTTTTTM
    TTTTTTM
    '''

else:
    print('Empty input file')
