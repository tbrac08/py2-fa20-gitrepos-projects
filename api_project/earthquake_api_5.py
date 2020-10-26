# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 21:50:25 2020

@author: tpbra
"""

##############################################################################
#  THis program allows you to see how many occured and where they occured
#############################################################################

#############################################################################
# imports needed for program
##############################################################################

import requests, json
from pprint import pprint


#   Getting the user data and building the api request
#############################################################################

def getting_user_data():
    
    print("Welcome to Thomas' earthquake program.")
    start_date = input("Please enter a start date in YYYY-MM-DD format: ")
    end_date = input("Please enter a end date in YYYY-MM-DD format : ")
    magnitude = float(input("Please enter a magnitude or 0 for all: "))
    
    return start_date, end_date, magnitude

##############################################################################
#   THis function will give you the total number of earthquakes that day
##############################################################################
    
def total_count(start_date, end_date):
    
     
    print("The total number of earthquakes for the day is below")
 
    # Builds api with a start and end time
    api_endpoint = "https://earthquake.usgs.gov/fdsnws/event/1/"
    count_test = "count?starttime=%s&endtime%s" % (start_date, end_date)
    url = api_endpoint + count_test

    data_request = requests.get(url)  #Makes data request from USGS
    #print(data_request.status_code)   #verifying valid data
    data_dump = json.loads(data_request.text) #Loads info into json
    print(data_dump)  #prints data to screen
    
##############################################################################
#  This function will run a query of the days earthquake information
##############################################################################
    
def magnitude_info(start_date, end_date, magnitude):
    
        
    print("The earthquake data for magnitude", magnitude, "is below")
 
    #Comments abouve apply below
    api_endpoint = "https://earthquake.usgs.gov/fdsnws/event/1/"
    test_reply = "query?format=geojson&starttime=%s&endtime%s" % (start_date, end_date)
    min_magnitude = "&minmagnitude=%s" % (magnitude)
    url = api_endpoint + test_reply + min_magnitude

    data_request = requests.get(url)
    #print(data_request.status_code)
    data_dump = json.loads(data_request.text)
    pprint(data_dump) #makes data dump more readable

##############################################################################
#  MAIN PROGRAM
##############################################################################
    
def main():
    
    start_date, end_date, magnitude = getting_user_data()
    magnitude_info(start_date, end_date, magnitude)
    total_count(start_date, end_date)
    
main()
    
    
    

        
        
        
        