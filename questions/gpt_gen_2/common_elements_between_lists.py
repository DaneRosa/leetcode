'''
3. Write a function that takes in two lists of integers and returns a new list containing the count of common elements between the two lists.
- This question assesses the candidate's ability to write a function, manipulate lists, and use conditional statements.

extra: 
compare each dict's ints
compare each sets ints

'''

import requests
import json
import pandas as pd
import numpy as np
import os
import flatten_json
from flatten_json import flatten

# rainforest data from downloads
file_path = '/Users/dosa/Downloads/rainforest_practice.json'

# open json file flatten then load data
def load_json_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)['features']
    # flatten the data to the top level
    flattened_data = [flatten(x) for x in data]
    return flattened_data

# function to collect all the ints within each dict and add to a list
def collect_list_of_ints(data):
    # data is a list of dicts
    list_of_integers = []
    for i in data: 
        indexed_ints = []
        # iterate over keys within each dict and if the v is an int add to it's own list
        for k,v in i.items():
            if isinstance(v, int):
                indexed_ints.append(v)
        list_of_integers.append(indexed_ints)
    return list_of_integers

# iterate over list of list and compare each one to the next
def compare_lists(list_of_integers):
    same_lists = []
    # compare list to next list
    for i in range(len(list_of_integers)-1):
        score = 0
        # compare each int in list to next list
        for i_val in list_of_integers[i]:
            if i_val in list_of_integers[i+1]:
                score += 1
            else:
                pass
        same_lists.append({i:score})
    return same_lists


    
# main
if __name__ == '__main__':
    # open json file to be used
    data = load_json_file(file_path)
    # collect all ints
    list_of_integers = collect_list_of_ints(data)
    # compare lists
    compare_lists(list_of_integers)

