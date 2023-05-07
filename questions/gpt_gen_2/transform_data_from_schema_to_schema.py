'''
- Write a Python script to transform data from one database schema to another.
This question tests your ability to build and maintain production data pipelines, which is a key responsibility of the role.
'''

import requests
import json
import pandas as pd
import numpy as np

# sample json data:
sample = {
    "name": "John",
    "age": 30,
    "cars": [
        {"name": "Ford", "models": ["Fiesta", "Focus", "Mustang"]},
        {"name": "BMW", "models": ["320", "X3", "X5"]},
        {"name": "Fiat", "models": ["500", "Panda"]}
    ],
    "address": {
        "street": "Main",
        "number": 123,
        "city": "New York"
    }
}

# list possible database schemas
# schemas = ['json', 'csv', 'xml', 'sql', 'nosql']

def transform_data(data):
    #  check to see what type of data we have
    if isinstance(data, dict):
        # normalize data
        print('Data is a dictionary.')
        normalized_data = pd.json_normalize(data)
        return normalized_data
    elif isinstance(data, list):
        print('Data is a list.')
        # transdform data from list to dataframe
        df = pd.DataFrame(data)
        return df
    else:
        print('Data type not supported.')

# main
if __name__ == '__main__':
    # transform data
    df = transform_data(sample)
    # print dataframe
    print(df)
