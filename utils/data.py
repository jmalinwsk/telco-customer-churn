import pandas as pd
from sklearn.decomposition import PCA
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
                'TotalCharges'],
            'missing_values': ['NA', 'na', 'n/a', 'N/A', 'null', 'NULL', '', '-', ' ', 'NaN'],
            'all_inputs': None,
            'all_classes': None,
            'train_inputs': None,
            'test_inputs': None,
            'train_classes': None,
            'test_classes': None,
            'all_inputs_2d': None
        }

    def get_data(self):
        self.values['all_values'] = pd.read_csv(
            'database/WA_Fn-UseC_-Telco-Customer-Churn.csv',
            na_values=self.values['missing_values']).drop(columns=['customerID'])

    def fill_missing_values(self):
        median = self.values['all_values'].median()
        self.values['all_values'] = self.values['all_values'].fillna(median)

    def get_all_inputs(self):
        self.values['all_inputs'] = self.values['all_values'][self.values['columns']].values

    def get_all_classes(self):
        self.values['all_classes'] = self.values['all_values']['Churn'].values

    def split_data(self):
        (self.values['train_inputs'], self.values['test_inputs'],
         self.values['train_classes'], self.values['test_classes']) = \
            train_test_split(self.values['all_inputs'], self.values['all_classes'], train_size=0.7)

    def encode_values(self):
        le = LabelEncoder()
        self.values['all_values']['gender'] = le.fit_transform(self.values['all_values']['gender'])
        self.values['all_values']['Partner'] = le.fit_transform(self.values['all_values']['Partner'])
        self.values['all_values']['Dependents'] = le.fit_transform(self.values['all_values']['Dependents'])
        self.values['all_values']['PhoneService'] = le.fit_transform(self.values['all_values']['PhoneService'])
        self.values['all_values']['MultipleLines'] = le.fit_transform(self.values['all_values']['MultipleLines'])
        self.values['all_values']['InternetService'] = le.fit_transform(self.values['all_values']['InternetService'])
        self.values['all_values']['OnlineSecurity'] = le.fit_transform(self.values['all_values']['OnlineSecurity'])
        self.values['all_values']['OnlineBackup'] = le.fit_transform(self.values['all_values']['OnlineBackup'])
        self.values['all_values']['DeviceProtection'] = le.fit_transform(self.values['all_values']['DeviceProtection'])
        self.values['all_values']['TechSupport'] = le.fit_transform(self.values['all_values']['TechSupport'])
        self.values['all_values']['StreamingTV'] = le.fit_transform(self.values['all_values']['StreamingTV'])
        self.values['all_values']['StreamingMovies'] = le.fit_transform(self.values['all_values']['StreamingMovies'])
        self.values['all_values']['Contract'] = le.fit_transform(self.values['all_values']['Contract'])
        self.values['all_values']['PaperlessBilling'] = le.fit_transform(self.values['all_values']['PaperlessBilling'])
        self.values['all_values']['PaymentMethod'] = le.fit_transform(self.values['all_values']['PaymentMethod'])
        self.values['all_values']['Churn'] = le.fit_transform(self.values['all_values']['Churn'])
