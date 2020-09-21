# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 20:20:54 2020

@author: tpbra
"""

##############################################################################
#   This program will convert a series of 1s and 0s into a picture 
##############################################################################

##############################################################################
#   Getting user information
##############################################################################

def GettingUserInfo():
    
    UserList = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,\
                0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0,\
                1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,\
                0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0,\
                0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    
    return UserList

#############################################################################
#  Number to Character change
#############################################################################

def Number_to_character_change(UserList):
    
    user_list_char = []
    loop_counter = 0
    
    for index in range(len(UserList)):
        if loop_counter != 10:
            if UserList[index] == 1:
                #print("x", end = " ")
                place_holder_x = "x"
                user_list_char.append(place_holder_x)
            else:
                #print("_", end = " ")
                place_holder_0 = " "
                user_list_char.append(place_holder_0)
    else:
        if UserList[index] == 1:
                #print("x", end = " ")
                place_holder_x = "x"
                user_list_char.append(UserList[index])
        else:
            #print("_", end = " ")
            place_holder_0 = " "
            user_list_char.append(UserList[index])
        loop_counter = 0        
    
    #print(user_list_char)
            
    return user_list_char

#############################################################################
# Printing the list into sections of three
##############################################################################
def DataManipulation(user_list_char):
#Counter = 0
    Counter_One = 0
    Counter_Two = 10
    
    while Counter_One != 100 and Counter_Two != 110:
        print(user_list_char[Counter_One:Counter_Two])
        Counter_One = Counter_One + 10
        Counter_Two = Counter_Two +10

##############################################################################
# Main Program
##############################################################################
def main():

    UserList = GettingUserInfo()
    user_list_char = Number_to_character_change(UserList)
    DataManipulation(user_list_char)

main()
    
    
    




    

    
    
    
    
    
    
    