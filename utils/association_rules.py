from mlxtend.frequent_patterns import apriori, association_rules


def apriori_module(data):
    items = apriori(data.values['onehot'], min_support=0.4, use_colnames=True, verbose=0)
    rules = association_rules(items, metric='confidence', min_threshold=0.8)
    print(rules)