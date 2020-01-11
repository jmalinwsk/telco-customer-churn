def count_values(data):
    print('\n\n - - AMOUNT OF DATA - -')
    print(data.values['all_values'].count())


def count_values_in_column(data):
    print('\n\n - - VALUES IN COLUMNS - -')
    for column in data.values['columns']:
        print(data.values['all_values'][column].value_counts(), '\n')


def mean(data):
    print('\n\n - - MEAN - -')
    print('tenure: ', data.values['all_values']['tenure'].mean())
    print('MonthlyCharges: ', data.values['all_values']['MonthlyCharges'].mean())
    print('TotalCharges: ', data.values['all_values']['TotalCharges'].mean())


def median(data):
    print('\n\n - - MEDIAN - -')
    print('tenure: ', data.values['all_values']['tenure'].median())
    print('MonthlyCharges: ', data.values['all_values']['MonthlyCharges'].median())
    print('TotalCharges: ', data.values['all_values']['TotalCharges'].median())


def std(data):
    print('\n\n - - STANDARD DEVIATION - -')
    print('tenure: ', data.values['all_values']['tenure'].std())
    print('MonthlyCharges: ', data.values['all_values']['MonthlyCharges'].std())
    print('TotalCharges: ', data.values['all_values']['TotalCharges'].std())


def min_value(data):
    print('\n\n - - MIN - -')
    print('tenure: ', data.values['all_values']['tenure'].min())
    print('MonthlyCharges: ', data.values['all_values']['MonthlyCharges'].min())
    print('TotalCharges: ', data.values['all_values']['TotalCharges'].min())


def max_value(data):
    print('\n\n - - MIN - -')
    print('tenure: ', data.values['all_values']['tenure'].max())
    print('MonthlyCharges: ', data.values['all_values']['MonthlyCharges'].max())
    print('TotalCharges: ', data.values['all_values']['TotalCharges'].max())
