import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from tensorflow import keras

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def decision_tree(data):
    print('\n\n - - DECISION TREE - -')
    dtc = DecisionTreeClassifier()
    dtc.fit(data.values['train_inputs'], data.values['train_classes'])
    y_pred = dtc.predict(data.values['test_inputs'])
    print('Accuracy: ', dtc.score(data.values['test_inputs'], data.values['test_classes']))
    print('Confusion matrix:\n', confusion_matrix(data.values['test_classes'], y_pred))


def naive_bayes(data):
    print('\n\n - - NAIVE BAYES - -')
    gnb = GaussianNB()
    gnb.fit(data.values['train_inputs'], data.values['train_classes'])
    y_pred = gnb.predict(data.values['test_inputs'])
    print('Accuracy: ', accuracy_score(data.values['test_classes'], y_pred))
    print('Confusion matrix:\n', confusion_matrix(data.values['test_classes'], y_pred))


def k_nn(data, neighbors):
    print('\n\n - - kNN (', neighbors, ') - -')
    knn = KNeighborsClassifier(n_neighbors=neighbors, metric='euclidean')
    knn.fit(data.values['train_inputs'], data.values['train_classes'])
    y_pred = knn.predict(data.values['test_inputs'])
    print('Accuracy: ', accuracy_score(data.values['test_classes'], y_pred))
    print('Confusion matrix:\n', confusion_matrix(data.values['test_classes'], y_pred))


def neural_network(data):
    print('\n\n - - NEURAL NETWORK - -')
    model = keras.Sequential()
    model.add(keras.layers.Input(shape=[19]))
    model.add(keras.layers.Dense(units=128, activation='relu'))
    model.add(keras.layers.Dense(units=3, activation='softmax'))
    model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(data.values['train_inputs'],
              data.values['train_classes'],
              validation_data=(data.values['test_inputs'], data.values['test_classes']),
              epochs=150,
              verbose=0)
    test_loss, test_acc = model.evaluate(data.values['test_inputs'], data.values['test_classes'], verbose=0)
    classes_pred = model.predict_classes(data.values['test_inputs'], verbose=0)
    print('Accuracy: ', test_acc)
    print('Confusion matrix:\n', confusion_matrix(data.values['test_classes'], classes_pred))


def random_forest(data):
    print('\n\n - - RANDOM FOREST - -')
    rf = RandomForestClassifier()
    rf.fit(data.values['train_inputs'], data.values['train_classes'])
    y_pred = rf.predict(data.values['test_inputs'])
    print('Accuracy: ', accuracy_score(data.values['test_classes'], y_pred))
    print('Confusion matrix:\n', confusion_matrix(data.values['test_classes'], y_pred))


def svm(data):
    print('\n\n - - SVM - -')
    svm = SVC(kernel='linear')
    svm.fit(data.values['train_inputs'], data.values['train_classes'])
    y_pred = svm.predict(data.values['test_inputs'])
    print('Accuracy: ', accuracy_score(data.values['test_classes'], y_pred))
    print('Confusion matrix:\n', confusion_matrix(data.values['test_classes'], y_pred))