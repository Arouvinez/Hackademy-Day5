import math

def three_numbers(x,y,z):
    a_list = []
    b_list = []
    if z == 0:
        return print("You cannot divide by 0!!")
    elif  x > y:
        return print("The first number has to be smaller than the second!")

    else:
        for i in range(x, y + 1):
            a_list.append(i)
            if a_list[i] % z == 0:
                b_list.append(i)
            else:
                continue

    return len(b_list)
