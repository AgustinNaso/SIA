import numpy as np

def to_bin_array(encoded_character: np.ndarray) -> np.ndarray:
    bin_array = np.zeros((7, 5), dtype=int)
    for row in range(0, 7):
        current_row = encoded_character[row]
        for col in range(0, 5):
            bin_array[row][4 - col] = current_row & 1
            current_row >>= 1
    return bin_array

def print_letter(array):
    for i in range(7):
        for j in range(5):
            if array[j+i*5] > 0.5:
                print("*",end="")
            else:
                print(" ",end="")
        print("")
    print("")