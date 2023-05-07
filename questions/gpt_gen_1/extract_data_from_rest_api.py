'''
- Write a Python script to extract data from a REST API endpoint and store it in a database.
This question tests your ability to build ETLs against REST endpoints, which is a required skill for the role.
'''
import requests
import json
import pandas as pd
import numpy as np

# Get data from API
rest_api_url = 'https://api.covid19api.com/summary'


def get_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return response.content.decode('utf-8')

def convert_to_df(data):
    # check to see if data is a dict
    if isinstance(data, dict):
        # normalize data
        normalized_data = pd.json_normalize(data)
        # df = pd.DataFrame.from_dict(normalized_data)
        return normalized_data

# main
if __name__ == '__main__':
    # get data from API
    data = get_data_from_api(rest_api_url)
    # convert data to dataframe
    df = convert_to_df(data)
    print(df)
