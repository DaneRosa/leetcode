'''
5. Write a function that takes in a string and checks if it is a palindrome.
- This question assesses the candidate's ability to write a function, manipulate strings, and use conditional statements.
'''

import json
import requests
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

# WOULD NEED TO CREATE A LIST OF STRINGS FROM DATA
# check if string is palindrome
def check_if_palindrome(string):
    # check if string is the same forwards and backwards
    if string == string[::-1]:
        return True
    else:
        return False

# main
if __name__ == '__main__':
    # open json file to be used
    data = load_json_file(file_path)
    