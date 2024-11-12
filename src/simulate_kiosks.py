import random
from threading import Lock

from locust import HttpUser, between, task

from src.dataset import generate_training_data
from src.datatypes import QueryInput

restaurants = [
    "Royal London",
    "Crystal Park",
    "Homberger Haus",
    "Restaurant Les Cèdres",
    "CSE MBDA L'Escale",
]

all_training_data = {restaurant: generate_training_data() for restaurant in restaurants}

user_lock = Lock()


class Kiosk(HttpUser):
    wait_time = between(0.01, 0.02)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with user_lock:
            self.restaurant = random.choice(restaurants)
            self.training_data = all_training_data[self.restaurant]

    @task
    def classify(self):
        query_input = QueryInput.random()
        self.client.get(
            "/classify",
            json={
                "training_data": self.training_data.model_dump(),
                "query_input": query_input.model_dump(),
            },
        )
