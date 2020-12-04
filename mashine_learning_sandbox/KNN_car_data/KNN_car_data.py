import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model, preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import shuffle
from tools import get_test_data


data = pd.read_csv("car.data")
print(f"Initial data head: \n {data.head()}")

label_encoder = preprocessing.LabelEncoder()
buying = label_encoder.fit_transform(list(data["buying"]))
maint = label_encoder.fit_transform(list(data["maint"]))
door = label_encoder.fit_transform(list(data["door"]))
persons = label_encoder.fit_transform(list(data["persons"]))
lug_boot = label_encoder.fit_transform(list(data["lug_boot"]))
safety = label_encoder.fit_transform(list(data["safety"]))
cls = label_encoder.fit_transform(list(data["class"]))

print(f"Transformed data from non-numerical to numerical (buying) {buying}")

predict = "class"

X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = get_test_data(X, y)

print(f"test data:\n x_train: {x_train}; \n x_test: {x_test};\n"
      f" y_train: {y_train}; \n y_test: {y_test};")

model = KNeighborsClassifier(n_neighbors=7)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(f"accuracy: {acc}")

predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

print(f"Predicted raw results:\n {predicted}")

for i in range(len(predicted)):
    print(f" Predicted: {names[predicted[i]]}, Actual: {names[y_test[i]]}, Data: {x_test[i]},")
    n = model.kneighbors([x_test[i]], 7)
    print(f" N: {n}\n")