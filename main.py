
import pandas as pd

from utils import preprocessing, statistics


def main():
    data = pd.read_csv('database/WA_Fn-UseC_-Telco-Customer-Churn.csv')

    all_inputs = preprocessing.get_inputs(data)
    all_classes = preprocessing.get_classes(data)


if __name__ == '__main__':
    main()
