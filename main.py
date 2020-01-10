from utils import preprocessing, statistics


def main():
    data = preprocessing.get_data()

    all_inputs = preprocessing.get_inputs(data)
    all_classes = preprocessing.get_classes(data)
    preprocessing.check_missing_values(data)

    #statistics.count_values(data)
    #statistics.count_values_in_column(data)


if __name__ == '__main__':
    main()
