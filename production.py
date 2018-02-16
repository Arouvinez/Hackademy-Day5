<<<<<<< Updated upstream
import pandas
a_list = [1,1,2,2]

=======
>>>>>>> Stashed changes

def remove_duplicates(a_list):
    b_list = [a_list[0]]
    for i in a_list:
        if i in b_list:
            continue
        else:
            b_list.append(i)
<<<<<<< Updated upstream

    return b_list
=======
    return b_list

    
>>>>>>> Stashed changes
