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
   #serNumber = 1
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
#   Data manipulation
##############################################################################

def DataManipulation(UserList):
    
    print(UserList[0:10])
    print(UserList[10:20])
    print(UserList[20:30])
    print(UserList[30:40])
    print(UserList[40:50])
    print(UserList[50:60])
    print(UserList[60:70])
    print(UserList[70:80])
    print(UserList[80:90])
    print(UserList[90:100])
                   
    
##############################################################################
#   Main Program
##############################################################################
    
def main():
    
    UserList = UserInfo()
    DataManipulation(UserList)
    
main()
    
    
    
    
    
    
    
    
    
    