from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier


def decision_tree(data):
    print('\n\n - - DECISION TREE - -')
    dtc = DecisionTreeClassifier()
    dtc.fit(data.values['train_inputs'], data.values['train_classes'])
    y_pred = dtc.predict(data.values['test_inputs'])
    print('Accuracy: ',dtc.score(data.values['test_inputs'], data.values['test_classes']))
    print('Confusion matrix:\n', confusion_matrix(data.values['test_classes'], y_pred))


def naive_bayes(data):
    print('\n\n - - NAIVE BAYES - -')
    gnb = GaussianNB()
    gnb.fit(data.values['train_inputs'], data.values['train_classes'])
    y_pred = gnb.predict(data.values['test_inputs'])
    print('Accuracy: ', accuracy_score(data.values['test_classes'], y_pred))
    print('Confusion matrix:\n', confusion_matrix(data.values['test_classes'], y_pred))
