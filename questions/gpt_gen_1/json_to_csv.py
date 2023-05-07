'''
turn json file into csv file
'''

import json
import requests
import pandas as pd
import numpy as np
import os
import csv

# function to open local json file:
def open_json_file(file_name):
    # open json file
    with open(file_name) as f:
        data = json.load(f)['features']
    return data

# function to turn json object into dataframe then into csv file:
def json_to_csv(data, file_name):
    # convert data to dataframe
    df = pd.DataFrame(data)
    # convert dataframe to csv file
    df.to_csv(file_name)
    return df

# main
if __name__ == '__main__':
    # open local json file of rainforest data from downloads folder
    file_name = os.path.join(os.path.expanduser('~'), 'Downloads', 'rainforest_practice.json')
    data = open_json_file(file_name)
    # turn json object into csv file
    df = json_to_csv(data, 'rainforest_data.csv')
    print(df)
