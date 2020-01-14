from utils import statistics, classificators, clustering, association_rules
from utils.data import Data


class Main:
    def __init__(self):
        self.data = Data()

    def main(self):
        self.data.get_data()
        self.data.fill_missing_values()
        self.data.onehot_values()

        statistics.count_values(self.data)
        statistics.count_values_in_column(self.data)
        statistics.mean(self.data)
        statistics.median(self.data)
        statistics.std(self.data)
        statistics.min_value(self.data)
        statistics.max_value(self.data)

        association_rules.apriori_module(self.data)

        self.data.encode_values()
        self.data.get_all_inputs()
        self.data.get_all_classes()
        self.data.split_data()
        classificators.decision_tree(self.data)
        classificators.naive_bayes(self.data)
        classificators.k_nn(self.data, 10)
        classificators.k_nn(self.data, 50)
        classificators.neural_network(self.data)
        classificators.random_forest(self.data)
        classificators.svm(self.data)


if __name__ == '__main__':
    Main().main()
