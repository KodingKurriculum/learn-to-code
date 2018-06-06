import pandas as pd
import requests
import io

_file = 'sample_data_frame.xlsx'
_url = "https://data.cityofnewyork.us/api/views/8u86-bviy/rows.csv"


def read_excel(file_name):
    # read from excel
    df = pd.read_excel(file_name, index_col=0)
    print(df)
    return df


def read_url(url):
    s = requests.get(url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')))
    #print(df)
    print(df.columns)
    return df


def print_mean(file_name):
    # find the average
    df = read_excel(file_name)
    average = df['units'].mean()
    print('Average units: {0}'.format(average))
    return df


def apply_function(file_name):
    # add a column and apply a function
    df = read_excel(file_name)
    df['multiple'] = df.units.apply(lambda x: 3 * x)
    print(df)
    return df


# Run the script - try calling print_mean(_file) or read_url(_url)
if __name__ == '__main__':
    read_excel(_file)
