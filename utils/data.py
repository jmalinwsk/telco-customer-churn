import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


class Data:
    def __init__(self):
        self.values = {
            'all_values': None,
            'columns': [
                    'gender',
                    'SeniorCitizen',
                    'Partner',
                    'Dependents',
                    'tenure',
                    'PhoneService',
                    'MultipleLines',
                    'InternetService',
                    'OnlineSecurity',
                    'OnlineBackup',
                    'DeviceProtection',
                    'TechSupport',
                    'StreamingTV',
                    'StreamingMovies',
                    'Contract',
                    'PaperlessBilling',
                    'PaymentMethod',
                    'MonthlyCharges',
                    'TotalCharges',
                    'Churn'],
            'missing_values': ['NA', 'na', 'n/a', 'N/A', 'null', 'NULL', '', '-', ' '],
            'all_inputs': None,
            'all_classes': None,
            'train_inputs': None,
            'test_inputs': None,
            'train_classes': None,
            'test_classes': None
        }

    def get_data(self):
        self.values['all_values'] = pd.read_csv(
            'database/WA_Fn-UseC_-Telco-Customer-Churn.csv',
            na_values=self.values['missing_values']).drop(columns=['customerID'])

    def fill_missing_values(self):
        median = self.values['all_values'].dropna().median()
        self.values['all_values'].fillna(median)

    def get_all_inputs(self):
        self.values['all_inputs'] = self.values['all_values'][self.values['columns']].values

    def get_all_classes(self):
        self.values['all_classes'] = self.values['all_values']['Churn'].values

    def split_data(self):
        (self.values['train_inputs'], self.values['test_inputs'],
         self.values['train_classes'], self.values['test_classes']) = \
            train_test_split(self.values['all_inputs'], self.values['all_classes'], train_size=0.7, random_state=1)
