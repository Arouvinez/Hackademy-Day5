import math

def three_numbers(x,y,z):
    a_list = []
    b_list = []

    for i in range(x, y + 1):
        a_list.append(i)
        if a_list[i] % z == 0:
            b_list.append(i)
        else:
            continue
    return len(b_list)
