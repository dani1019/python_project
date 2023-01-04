import information as info
from random import *
#randomly select compare A and AgainB
def random_select():
    #get key of inform_list (get name)
    selected_list = sample(list(info.inform_list.keys()),2)
    print(f"selected_list:  {selected_list}")

    return selected_list

def print_subject(selected_list)