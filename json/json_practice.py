# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 21:04:32 2020

@author: tpbra
"""

##############################################################################
#   JSON practice
##############################################################################

import json

dogs_dict = {"dogs":
            [{"name": "Remi", "breed": "Rottweiler", "age": 4},
             {"name": "Wags", "breed": "Pit Bull", "age": 10},
             {"name": "Blue", "breed": "Cattle Dog", "age": 1},
             {"name": "Gordie", "breed": "Pit Bull", "age": 11}]}
            
with open("dogs.json", "w") as dogs:
    json.dump(dogs_dict, dogs)
    
with open("dogs.json", "r") as dogs:
    print(json.dumps(json.load(dogs), indent = 4))
            


