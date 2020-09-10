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
#   Printing the list into sections of three
##############################################################################
    
def DataManipulation(UserList):
    
    #Counter = 0
    print(UserList[0:3])
    print(UserList[3:6])
    print(UserList[6:9])
    
##############################################################################
#   Main Program
##############################################################################
    
def main():
    
    UserList = GettingUserInfo()
    DataManipulation(UserList)
    
main()
    
    
    
    
    
    
    