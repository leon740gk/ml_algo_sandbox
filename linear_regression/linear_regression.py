import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
from sklearn import linear_model

from tools import get_test_data


def train_linear_model(training_times, best_acc=0):
    for i in range(training_times):
        x_train, x_test, y_train, y_test = get_test_data(X, y)
        linear_data_model = linear_model.LinearRegression()
        linear_data_model.fit(x_train, y_train)
        acc = linear_data_model.score(x_test, y_test)
        print(acc)
        if acc > best_acc:
            best_acc = acc
            with open("linear_student_model.pickle", "wb") as f:
                pickle.dump(linear_data_model, f)

def plotter(first_param, plot_style="ggplot"):
    style.use(plot_style)
    plt.scatter(data[first_param], data[predict])
    plt.xlabel(first_param)
    plt.ylabel("Final grade")
    plt.show()

data = pd.read_csv("student-mat.csv", sep=";")
data_params = ["G1", "G2", "G3", "studytime", "failures", "absences"]
predict = "G3"
data = data[data_params]

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = get_test_data(X, y)

# Training model block
# train_linear_model(740)

with open("linear_student_model.pickle", "rb") as f:
    linear_data_model = pickle.load(f)

predictions = linear_data_model.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

# drawing data of correlation
for i in data_params:
    if i != predict:
        plotter(first_param=i)
