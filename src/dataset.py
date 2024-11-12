import numpy as np

from src.datatypes import TrainingData


def generate_training_data(
    xmin: int = -10,
    xmax: int = 10,
    ymin: int = 0,
    ymax: int = 3,
    num_samples: int = 10,
    num_features: int = 2,
) -> TrainingData:
    """Generate random training data.

    Args:
        xmin (int, optional): Defaults to -10.
        xmax (int, optional): Defaults to 10.
        ymin (int, optional): Defaults to 0.
        ymax (int, optional): Defaults to 3.
        num_samples (int, optional): Defaults to 10.
        num_features (int, optional): Defaults to 2.

    Returns:
        TrainingData: the generated training data
    """
    training_data = np.concatenate(
        [
            np.random.randint(xmin, xmax, (num_samples, num_features)),
            np.random.randint(ymin, ymax, num_samples)[:, None],
        ],
        axis=1,
    )
    return TrainingData(training_data=training_data.tolist())
