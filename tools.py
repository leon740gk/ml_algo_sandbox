import sklearn


def get_test_data(X, y):
    return sklearn.model_selection.train_test_split(X, y, test_size=0.1)
