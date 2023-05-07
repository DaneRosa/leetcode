'''
- Write a Python function to calculate the average of a column in a large dataset.
This question tests your SQL skills, which are also required for the role.

adds: 
- get max canopy from json file
- get average of max canopy
- get min max canopy
'''

import json
import requests
import pandas as pd
import numpy as np
import os

# function to open local json file:
def open_json_file(file_name):
    # open json file
    with open(file_name) as f:
        data = json.load(f)['features']
    return data

# function to calculate average of a column in a large dataset:
def avg_column_in_large_dataset(data, column_name):
    # create empty list to store values of column
    column_values = []
    # loop through each row in data
    for row in data:
        # append value of column to column_values list
        column_values.append(row['properties'][column_name])
    # calculate average of column_values list
    avg = np.mean(column_values)
    return avg 
    

# main
if __name__ == '__main__':
    # open local json file of rainforest data from downloads folder
    file_name = os.path.join(os.path.expanduser('~'), 'Downloads', 'rainforest_practice.json')
    data = open_json_file(file_name)
    pass
    # calculate average of 'area' column
    avg = avg_column_in_large_dataset(data, 'maxCanopy')
    print(f'the average max canopy is {avg}')