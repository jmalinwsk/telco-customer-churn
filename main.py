from utils import statistics
from utils.data import Data


class Main:
    def __init__(self):
        self.data = Data()

    def main(self):
        self.data.get_data()
        self.data.fill_missing_values()
        self.data.get_all_inputs()
        self.data.get_all_classes()

        statistics.count_values(self.data)
        statistics.count_values_in_column(self.data)
        statistics.mean(self.data)
        statistics.median(self.data)
        statistics.std(self.data)
        statistics.min_value(self.data)
        statistics.max_value(self.data)


if __name__ == '__main__':
    Main().main()
