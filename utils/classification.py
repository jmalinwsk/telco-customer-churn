from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier


def decision_tree(data):
    dtc = DecisionTreeClassifier()
    dtc.fit(data.values['train_inputs'], data.values['train_classes'])
    print(dtc.score(data.values['test_inputs'], data.values['test_classes']))
    print(metrics.confusion_matrix(data.values['all_classes'], dtc.predict(data.values['all_inputs'])))
