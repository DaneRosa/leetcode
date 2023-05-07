'''
6. Write a function that takes in a list of integers and returns the second smallest number in the list.
- This question assesses the candidate's ability to write a function, manipulate lists, and use conditional statements.
'''

import json
import requests
import pandas as pd
import numpy as np
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

# create list of integers from data
def create_list_of_integers(data):
    # create empty list
    list_of_integers = []
    # get k,v from each dict within list
    for k,v in data.items():
        # check if value is an integer
        if isinstance(v, int):
            # append integer to list
            list_of_integers.append(v)
    # keep only unique integers
    list_of_integers = list(set(list_of_integers))
    return list_of_integers


# main  
if __name__ == '__main__':
    # open json file to be used
    data = load_json_file(file_path)
    # create list of integers from data
    list_of_integers = create_list_of_integers(data)
    # print second smallest number in list
    print(sorted(list_of_integers)[1])
