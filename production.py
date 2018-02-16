import pandas
a_list = [1,1,2,2]


def remove_duplicates(a_list):
    b_list = [a_list[0]]
    for i in a_list:
        if i in b_list:
            continue
        else:
            b_list.append(i)

    return b_list
