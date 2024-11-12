import time

import numpy as np
import uvicorn
import xxhash
from cachetools import cached

from fastapi import (
    FastAPI,
    Depends
)
from fastapi.responses import PlainTextResponse
from pydantic import Field
from pydantic_settings import BaseSettings
from sklearn.neighbors import KNeighborsClassifier

from src.inference import inference

from src.training import fit_model

from src.datatypes import (
    QueryInput,
    TrainingData,
    ClassificationResult
)

app = FastAPI()


class TimedContext:

    def __init__(self, context_holder):
        self._context_holder = context_holder
        self._start_time = None

    def _current_time(self):
        return time.time()

    def __enter__(self):
        self._start_time = self._current_time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{self._context_holder.__name__} took {self._current_time() - self._start_time} seconds')


def timed(func):
    def _timed(*args, **kwargs):
        with TimedContext(func):
            return func(*args, **kwargs)
    return _timed


@timed
def hash_training_data(training_data: np.array) -> int:
    h = xxhash.xxh64()
    h.update(training_data)
    return h.intdigest()


def get_training_data_as_np_array(training_data: TrainingData) -> np.array:
    with TimedContext(get_training_data_as_np_array):
        return np.asarray(training_data.training_data)


@cached({}, key=hash_training_data)
def k_neighbors_classifier(training_data: np.array = Depends(get_training_data_as_np_array)):
    with TimedContext(k_neighbors_classifier):
        return fit_model(training_data)


@app.get('/ping')
def ping():
    return PlainTextResponse('OK')


@app.get('/classify')
async def classify(query_input: QueryInput, model: KNeighborsClassifier = Depends(k_neighbors_classifier)) -> ClassificationResult:
    return inference(query_input, model)


class AppSettings(BaseSettings):
    port: int = Field(alias='APP_PORT', default=8000)
    worker_count: int = Field(alias='APP_WORKER_COUNT', default=12)


if __name__ == '__main__':
    settings = AppSettings()
    uvicorn.run('src.run_server:app', port=settings.port, workers=settings.worker_count)

