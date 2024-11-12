import time

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

from src.datatypes import ClassificationResult, QueryInput


def inference(
    query_input: QueryInput, model: KNeighborsClassifier
) -> ClassificationResult:
    """Classify query input (or batch of inputs) with a fitted model.

    Args:
        query_input (QueryInput): the query input(s) to classify.
        model (KNeighborsClassifier): the fitted model.

    Returns:
        ClassificationResult: the classification result.
    """
    query_input_np = np.array(query_input.query_input)
    number_of_queries = query_input_np.shape[0]

    wait_time_sec = 0.2 + 0.05 * (number_of_queries - 1)
    time.sleep(wait_time_sec)

    y_pred = model.predict(np.atleast_2d(query_input_np))
    cls_result = ClassificationResult(classification_result=y_pred.tolist())
    return cls_result
