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
    
    UserList = [1, 1, 1, 0, 1, 0, 0, 1, 0]
    
    return UserList

#############################################################################
#  Number to Character change
#############################################################################

def Number_to_character_change(UserList):
    
    user_list_char = []
    
    for index in range(len(UserList)):
        if UserList[index] == 1:
            print("x")
            user_list_char.append(UserList)
        else:
            print("_")
            user_list_char.append(UserList)
            
    print(user_list_char)
            
    return user_list_char

#############################################################################
# Printing the list into sections of three
##############################################################################
#def DataManipulation(user_list_char):
#Counter = 0
    #print(user_list_char[0:3])
    #print(user_list_char[3:6])
   # print(user_list_char[6:9])

##############################################################################
# Main Program
##############################################################################
def main():

    UserList = GettingUserInfo()
    user_list_char = Number_to_character_change(UserList)
    #DataManipulation(user_list_char)

main()
    
    
    




    

    
    
    
    
    
    
    