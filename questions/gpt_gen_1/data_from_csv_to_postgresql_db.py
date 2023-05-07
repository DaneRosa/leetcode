'''
- Write a Python script to read data from a CSV file and insert it into a PostgreSQL database.
This question tests your ability to work with different types of data sources and databases, which is a valuable skill for a data engineer.
'''

import pandas as pd
import numpy as np
import requests
import os
import csv
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine




# function to open local csv file:
def open_csv_file(file_name):
    # open csv file
    with open(file_name) as f:
        data = csv.reader(f)
        # convert csv data to list
        data = list(data)
    return data

# function to insert data into postgresql database:
def insert_data_into_postgresql_db(data, table_name):
    # create engine
    engine = create_engine('postgresql://postgres:password@localhost:5432/postgres')
    # convert data to dataframe
    df = pd.DataFrame(data)
    # insert data into postgresql database
    df.to_sql(table_name, engine, if_exists='replace')
    return df

# main
if __name__ == '__main__':
    # open local csv file from current directory
    file_name = '/Users/dosa/leetcode/questions/.rainforest_data.csv'
    data = open_csv_file(file_name)
    # insert data into postgresql database
    df = insert_data_into_postgresql_db(data, 'rainforest_data')
    print(df)
