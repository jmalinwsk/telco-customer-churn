import pandas

from utils import data_properties


def count_values(data):
    print('\n\n - - AMOUNT OF DATA - -')
    print(data.count())


def count_values_in_column(data):
    print('\n\n - - VALUES IN COLUMNS - -')
    for column in data_properties.columns:
        print(data[column].value_counts(), '\n')


def mean(data):
    print('\n\n - - MEAN - -')
    print(data_properties.columns[5], ': ', data[data_properties.columns[5]].mean())
    print(data_properties.columns[18], ': ', data[data_properties.columns[18]].mean())
    print(data_properties.columns[19], ': ', data[data_properties.columns[19]].mean())


def median(data):
    print('\n\n - - MEDIAN - -')
    print(data_properties.columns[5], ': ', data[data_properties.columns[5]].median())
    print(data_properties.columns[18], ': ', data[data_properties.columns[18]].median())
    print(data_properties.columns[19], ': ', data[data_properties.columns[19]].median())


def std(data):
    print('\n\n - - STANDARD DEVIATION - -')
    print(data_properties.columns[5], ': ', data[data_properties.columns[5]].std())
    print(data_properties.columns[18], ': ', data[data_properties.columns[18]].std())
    print(data_properties.columns[19], ': ', data[data_properties.columns[19]].std())


def min_value(data):
    print('\n\n - - MIN - -')
    for column in data_properties.columns:
        print(column, ': ', data[column].min())


def max_value(data):
    print('\n\n - - MIN - -')
    for column in data_properties.columns:
        print(column, ': ', data[column].max())



