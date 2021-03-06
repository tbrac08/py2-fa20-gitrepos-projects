# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:08:11 2020

@author: tpbra
"""
import csv
import pandas as pd
import requests, json
from pprint import pprint

##############################################################################
#  THis program allows you to see how many occured and where they occured
#############################################################################

#############################################################################
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
    import requests, json

    print("The total number of earthquakes for the day is below")

    # Builds api with a start and end time
    api_endpoint = "https://earthquake.usgs.gov/fdsnws/event/1/"
    count_test = "count?starttime=%s&endtime%s" % (start_date, end_date)
    url = api_endpoint + count_test

    data_request = requests.get(url)  # Makes data request from USGS
    # print(data_request.status_code)   #verifying valid data
    data_dump = json.loads(data_request.text)  # Loads info into json
    print(data_dump)  # prints data to screen


##############################################################################
#  This function will run a query of the days earthquake information
##############################################################################

def magnitude_info(start_date, end_date, magnitude):

    print("The earthquake data for magnitude", magnitude, "is below")

    # Comments abouve apply below
    api_endpoint = "https://earthquake.usgs.gov/fdsnws/event/1/"
    test_reply = "query?format=geojson&starttime=%s&endtime%s" % (start_date, end_date)
    min_magnitude = "&minmagnitude=%s" % (magnitude)
    url = api_endpoint + test_reply + min_magnitude

    data_request = requests.get(url)
    # print(data_request.status_code)
    data_dump = json.loads(data_request.text)
    return data_dump


##############################################################################
#  Creating a csv file
##############################################################################




##############################################################################
#  Printing the data
##############################################################################
    
def print_data_dump(data_dump):
    earthquakes = data_dump["features"]  #Finds main data feature to print

    for earthquake in earthquakes:
        p = earthquake["properties"]   #finds subclasses of features to print
        print(\
f"""Place: {p["place"]}
    Alert: {p["alert"]}
    Felt: {p["felt"]}
    Magnitude: {p["mag"]}
    Tsunami: {p["tsunami"]}
    
"""
)
        
##############################################################################
#  MAIN PROGRAM
##############################################################################

def main():
    start_date, end_date, magnitude = getting_user_data()
    data_dump = magnitude_info(start_date, end_date, magnitude)
    print_data_dump(data_dump)
    total_count(start_date, end_date)


main()