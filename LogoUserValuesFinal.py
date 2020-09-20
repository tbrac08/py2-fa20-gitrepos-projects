 # -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 21:11:58 2020

@author: tpbra
"""

##############################################################################
#   This program will take a 10x10 group of 1s and 0s and make it into the 
#   logo TB
#############################################################################

#############################################################################
#   Getting the user info
#############################################################################

def UserInfo():
    
    UserList = []
    Counter = 0
        
    print("We are going to make a logo using 1s and 0s.")
    UserNumber = input("Please enter a 1 or a 0. ")
   
    while Counter != 100:
        if UserNumber == "1" or UserNumber == "0":
            UserList.append(UserNumber)
            Counter = Counter + 1
            UserNumber = input("Please enter a 1 or a 0. ")
        else:  
            print("You must enter a 1 or 0.")
            UserNumber = input("Please enter a 1 or a 0. ")
        
           
         
    
    return UserList

##############################################################################
#   Changing the numbers to characters
##############################################################################
    
def Number_to_character_change(UserList):
    
    user_list_char = []
    
    
    for index in range(len(UserList)):
        if UserList[index] == "1":
            place_holder_x = "x"
            user_list_char.append(place_holder_x)
        else:
            place_holder_0 = " "
            user_list_char.append(place_holder_0)
   
      
    return user_list_char




##############################################################################
#   Data manipulation
##############################################################################

def DataManipulation(user_list_char):
    
    Counter_One = 0
    Counter_Two = 10
    
    while Counter_One != 100 and Counter_Two != 110:
        print(user_list_char[Counter_One:Counter_Two])
        Counter_One = Counter_One + 10
        Counter_Two = Counter_Two +10    
    
                      
    
##############################################################################
#   Main Program
##############################################################################
    
def main():
    
    UserList = UserInfo()
    user_list_char = Number_to_character_change(UserList)
    DataManipulation(user_list_char)
    
main()
    
    
    
    
    
    
    
    
    
    