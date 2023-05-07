'''
1. Write a function that takes in a list of integers and returns the sum of all even numbers in the list.
- This question assesses the candidate's ability to write a function, manipulate lists, and use conditional statements.


extra: 
turn it into a df then get the sum of the column
'''

import json
import pandas as pd
import numpy as np
import os

# rainforest data from downloads
file_path = '/Users/dosa/Downloads/rainforest_practice.json'

# open json file and load data
def load_json_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)['features'] 
    return data

# create function to return sum of all even numbers in the list
def sum_of_evens_in_loi(list_of_integers):
    sum_of_evens = 0
    for i in list_of_integers:
        if i % 2 == 0:
            sum_of_evens += i
    return sum_of_evens

# find second smallest number in a list of ints
def second_smallest(list_of_integers):
    # sort the list
    list_of_integers.sort()
    # return the second value in the list
    return list_of_integers[1]


# main
if __name__ == '__main__':
    # load data
    data = load_json_file(file_path)

    # create list of integers from data
    list_of_integers = []
    # iterate through data and append maxCanopy to list_of_integers if the value is even
    for i in data: 
        # round to the nearest whole number
        maxCanopy = round(i['properties']['maxCanopy'])
        if round(maxCanopy) % 2 == 0:
            list_of_integers.append(maxCanopy)
    
    sum_return = sum_of_evens_in_loi(list_of_integers)

    # second smallest number in a list of ints
    second_smallest = second_smallest(list_of_integers)