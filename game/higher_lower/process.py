import information as info
from random import *
#randomly select compare A and AgainB
def random_select():
    #get key of inform_list (get name)
    selected_list = sample(list(info.inform_list.keys()),2)
    return selected_list

#
def print_subject(selected_list):
    comparison_data = []
    comparison_list = []
    for index,name in enumerate(selected_list) :
        person_inform = info.inform_list[name]
        comparison_data.append(name)
        comparison_data.append(person_inform[2])
        comparison_list.append(comparison_data)
        if index == 0:
            print(f"compare A: {person_inform[0]}, from {person_inform[1]}")
        else:
            print("vs")
            print(f"Against A: {person_inform[0]}, from {person_inform[1]}")           

    selected_person = input("Who has more followers? Type 'A' or 'B': ")

    return selected_person,comparison_list

def operate_comparison(selected_person,comparison_list):
    for element in comparison_list:
        print(element)

