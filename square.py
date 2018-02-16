import math

def square(a_list):
    square_list = []
    for each_element in range(0,len(a_list)):
        square_list.append(math.pow(each_element,2))
    return square_list
