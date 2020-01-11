from utils import statistics, classification
from utils.data import Data


class Main:
    def __init__(self):
        self.data = Data()

    def main(self):
        self.data.get_data()
        self.data.fill_missing_values()
        self.data.encode_values()
        self.data.get_all_inputs()
        self.data.get_all_classes()
        self.data.split_data()

        statistics.count_values(self.data)
        statistics.count_values_in_column(self.data)
        statistics.mean(self.data)
        statistics.median(self.data)
        statistics.std(self.data)
        statistics.min_value(self.data)
        statistics.max_value(self.data)

        self.data.values['all_values'].to_csv('plik.csv')
        classification.decision_tree(self.data)
        classification.naive_bayes(self.data)


if __name__ == '__main__':
    Main().main()
