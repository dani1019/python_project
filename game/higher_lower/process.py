import information as info
from random import *
#randomly select compare A and AgainB
def random_select():
    #get key of inform_list (get name)
    selected_list = sample(list(info.inform_list.keys()),2)
    return selected_list

#
def print_subject(selected_list):
    only_comparison_data = {}
    comparison_data_list = []
    for index,name in enumerate(selected_list) :
        person_inform = info.inform_list[name]
        comparison_data_list.append(person_inform[2])
        if index == 0:
            print(f"compare A: {person_inform[0]}, from {person_inform[1]}")
            comparison_data_list.append("A")
        else:
            print("vs")
            print(f"Against A: {person_inform[0]}, from {person_inform[1]}")
            comparison_data_list.append("B")
    
        #각 name key에, 각각의 comparison_data_list만 넣도록 수정하기 220110이후 작업
        only_comparison_data[name] = comparison_data_list

    selected_person = input("Who has more followers? Type 'A' or 'B': ")

    return selected_person,only_comparison_data

def operate_comparison(selected_person,only_comparison_data):
    for name, number in only_comparison_data.items():
        print(name, number)
