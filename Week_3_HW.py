0# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:00:20 2020

@author: tpbra
"""

#############################################################################
#    Week three warm up 1
##############################################################################

def main():
    
    #NumbersFile = open("Numbers.txt", "w")
    NumberList = []
    IndexCounter = 10
    LoopCounter = 0
    NumberCounter = 0
    
    Number = input("Enter the numbers 0 through 9. ")
    
    while NumberCounter != 10:
        NumberList.append(Number)
        NumberCounter = NumberCounter + 1
        Number = input("Enter the numbers 0 through 9. ")        
    
    while LoopCounter != 10:
        print(NumberList[0:IndexCounter])
        #NumbersFile.write(NumberList)
        LoopCounter = LoopCounter + 1
        IndexCounter = IndexCounter - 1
        
    #NumbersFile.close
        
main ()   
    
    
    
    
    