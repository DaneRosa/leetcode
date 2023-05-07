'''
2. Write a function that takes in a string and returns the reverse of the string.
- This question assesses the candidate's ability to write a function and manipulate strings.

extras:
overwite original values with reversed values
'''

import requests
import json
import pandas as pd
import numpy as np
import os
import flatten_json
from flatten_json import flatten

file_path = '/Users/dosa/Downloads/rainforest_practice.json'

# func to turn json into df
def json_to_df(file_path):
    data = json.load(open(file_path))['features']
    flattened_data = [flatten(d) for d in data]
    df = pd.DataFrame(flattened_data)
    return df

# func to reverse string
def reverse_string(data):
    # find strings in df (str = object)
    string_columns = data.select_dtypes(include=['object']).columns
    # get the values from the first column in the string_columns list
    string_values = data[string_columns[0]].values
    # reverse each string
    reversed_strings = [string[::-1] for string in string_values]

# main
if __name__ == '__main__':
    # load data
    data = json_to_df(file_path)
    reverse_string(data)