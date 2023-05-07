'''
4. Write a function that takes in a list of strings and returns the longest string in the list.
- This question assesses the candidate's ability to write a function, manipulate lists, and use conditional statements.

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

# collect string from each dict within flattened data
def collect_list_of_strings(data):
    # data is a list of dicts
    list_of_strings = []
    for i in data: 
        # iterate over keys within each dict and if the v is an int add to it's own list
        for k,v in i.items():
            if isinstance(v, str):
                list_of_strings.append({
                    'value':v,
                    'length':len(v), 
                    'uid:':i['id']
                    })
    '''
    creates a new list of unique dictionaries from an input list containing dictionaries with potential duplicate key-value pairs
    list_of_strings = [dict(t) for t in {tuple(d.items()) for d in list_of_strings}]
    may not want this ^ because has no unique key
    '''
    return list_of_strings

# find the longest string in the list
def find_longest_string(list_of_strings):
    # sort list of dicts by length
    sorted_list = sorted(list_of_strings, key=lambda k: k['length'])
    # return last item in list
    longest_string = sorted_list[-1]
    return longest_string
# main
if __name__ == '__main__':
    # load data
    data = load_json_file(file_path)
    # collect list of strings
    list_of_strings = collect_list_of_strings(data)
    # find longest string
    longest_string = find_longest_string(list_of_strings)
    