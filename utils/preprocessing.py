import pandas as pd

from utils import data_properties


def get_data():
    return pd.read_csv('database/WA_Fn-UseC_-Telco-Customer-Churn.csv',
                       na_values=data_properties.missing_values)


def get_inputs(data):
    return data[data_properties.columns[:-1]].values


def get_classes(data):
    return data[data_properties.columns[-1]].values


def check_missing_values(data):
    print(data.isna().any())