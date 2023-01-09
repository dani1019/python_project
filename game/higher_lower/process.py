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
    comparison_data_A = []
    comparison_data_B = []
    for index,name in enumerate(selected_list) :
        person_inform = info.inform_list[name]

        if index == 0:
            print(f"compare A: {person_inform[0]}, from {person_inform[1]}")
            comparison_data_A.append(name)
            comparison_data_A.append(person_inform[2])
            only_comparison_data["A"] = comparison_data_A
        else:
            print("vs")
            print(f"Against A: {person_inform[0]}, from {person_inform[1]}")
            comparison_data_B.append(name)
            comparison_data_B.append(person_inform[2])
            only_comparison_data["B"] = comparison_data_B

    selected_person = input("Who has more followers? Type 'A' or 'B': ")

    return selected_person,only_comparison_data

def operate_comparison(selected_person,only_comparison_data):
    for name, inform in only_comparison_data.items():
        if selected_person == "A":
            if only_comparison_data["A"][1] >  only_comparison_data["B"][1]:
                print(f"you are correct. {only_comparison_data["A"][0]}  is more famous.")
            else:
                print("you are wrong.")