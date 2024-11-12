import numpy as np
import pydantic


class TrainingData(pydantic.BaseModel):
    training_data: list[list[int]]


class QueryInput(pydantic.BaseModel):
    query_input: list[int | list[int]]

    @classmethod
    def random(cls):
        return cls(query_input=np.random.randint(-10, 10, 2).tolist())


class ClassificationResult(pydantic.BaseModel):
    classification_result: list[int]
