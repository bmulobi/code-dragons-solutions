import math
import numpy as np

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

def check_slice(min, slice):
    flat_slice =
    return

lines = get_file_contents("medium.in")

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

    # use various shapes to attempt for max_slices (the goal)
    for shape in shapes:
        # def cut_slices(shape):
        num_rows = int(shape[0])
        num_cols = int(shape[1])
        start_row = 0
        end_row = num_rows

        horizontal_steps = int(math.floor(cols / num_cols))
        vertical_steps = int(math.floor(rows / num_rows))

        for v_step in range(0, vertical_steps):
            start_col = 0
            end_col = num_cols
            
            for h_step in range(0, horizontal_steps):
                slice = pizza[start_row:end_row, start_col:end_col]

                is_ok = check_slice(slice)

                start_col = end_col
                end_col += num_cols

            start_row = end_row
            end_row += num_rows

        break


        #for
        # cut from top left horizontally





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
