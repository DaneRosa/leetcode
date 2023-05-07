'''
data from amazon rainforest
'''
# open local json file of rainforest data

import json
import requests
import pandas as pd
import numpy as np
import os

def open_json_file(file_name):
    # open json file
    with open(file_name) as f:
        data = json.load(f)['features']
    return data

# main
if __name__ == '__main__':
    # open local json file of rainforest data from downloads folder
    file_name = os.path.join(os.path.expanduser('~'), 'Downloads', 'rainforest_practice.json')
    data = open_json_file(file_name)
    