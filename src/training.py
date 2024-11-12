import time

import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def fit_model(training_data: np.ndarray) -> KNeighborsClassifier:
    """Fit a model to the training data.

    With a fitted model, we can classify query inputs.
    Example:
    >>> training_data = generate_training_data()
    >>> model = fit_model(training_data.training_data)
    >>> query_input = QueryInput.random()
    >>> result = inference(query_input, model)

    Args:
        training_data (np.ndarray): Training data with shape (num_samples, num_features + 1).

    Returns:
        KNeighborsClassifier: A fitted model.
    """
    print("fitting model")
    time.sleep(2)  # 2 sec for mimicking a compute heavy task
    model = KNeighborsClassifier(n_neighbors=3).fit(
        training_data[:, :-1], training_data[:, -1]
    )
    print("end fitting model")
    return model
