import pandas as pd


class Data:
    def __init__(self):
        self.values = {
            'all_values': None,
            'columns': [
                    'customerID',
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
            'all_classes': None
        }

    def get_data(self):
        self.values['all_values'] = pd.read_csv(
            'database/WA_Fn-UseC_-Telco-Customer-Churn.csv',
            na_values=self.values['missing_values'])

    def fill_missing_values(self):
        median = self.values['all_values'].dropna().median()
        self.values['all_values'].fillna(median)

    def get_all_inputs(self):
        self.values['all_inputs'] = self.values['all_values'][:-1].values

    def get_all_classes(self):
        self.values['all_classes'] = self.values['all_values']['Churn'].values

