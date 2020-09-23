# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:15:11 2020

@author: tpbra
"""

#############################################################################
#    Names Hausaufgabe
#############################################################################

#############################################################################
#   Reading data file into the program
##############################################################################

def getting_data():
    
    data_file = open("names.txt", "r")
    names_list = []

    person_name = data_file.readline().rstrip("\n")
        
    while person_name != "":
        names_list.append(person_name)
        person_name = data_file.readline().rstrip("\n")
        
     
    return names_list

###############################################################################
#  Splitting the names
###############################################################################
    
def name_splitting(names_list):
    
    name_list_split = []
    name_counter = 0
    
    name_holder = names_list[0]
    
    for index in range(len(names_list)):
        name_holder_split = name_holder.split()
        name_list_split.append(name_holder_split)
        print(name_list_split)
        name_counter = name_counter + 1
        name_holder = names_list[name_counter]
        
    return name_list_split

##############################################################################
#   Printing values
##############################################################################
    
def display_values(name_list_split):
    
    first_name_counter = 0
    last_name_counter = 1
    
    for index in range(len(name_list_split)):
        print("Good evening Dr.", name_list_split[last_name_counter], \
              "would you mind, if I called you", \
              name_list_split[first_name_counter], "?")
        first_name_counter = first_name_counter + 2
        last_name_counter = last_name_counter + 2
        
##############################################################################
#   Main Program
##############################################################################

def main(): 
    
    
    names_list = getting_data()
    name_list_split = name_splitting(names_list)
    display_values(name_list_split)
    
    
main()
    
