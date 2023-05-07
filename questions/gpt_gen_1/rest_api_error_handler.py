'''
- Write a Python function to handle errors when reading data from a REST API endpoint.
This question tests your ability to troubleshoot and handle errors in a production data pipeline.

'''

import requests
import json
import pandas as pd

# Get data from API
rest_api_url = 'https://api.covid19api.com/summary'

def handle_api_responses(url):
    response = requests.get(url)
    # check to see if status code begins with a 5
    if str(response.status_code)[0] == '5':
        # raise an exception
        raise Exception('Server Error')
    # check to see if status code begins with a 4
    elif str(response.status_code)[0] == '4':
        # raise an exception
        raise Exception('Client Error')
    # check to see if status code begins with a 3
    elif str(response.status_code)[0] == '3':
        # raise an exception
        raise Exception('Redirect Error')
    # check to see if status code begins with a 2
    elif str(response.status_code)[0] == '2':
        # return data
        return json.loads(response.content.decode('utf-8'))
    else:
        # raise an exception
        raise Exception('Unknown Error')

# main
if __name__ == '__main__':
    # get data from API
    data = handle_api_responses(rest_api_url)
    # convert data to dataframe
    df = pd.json_normalize(data)
    print(df)

