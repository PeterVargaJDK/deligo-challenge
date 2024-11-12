# Deligo Inference Backend Service Assignment

## Introduction

In this assignment you are tasked to create a backend service that runs ML model training and inference, serving a number of [Deligo Kiosks](https://www.deligovision.com/canteens) (our automated checkout devices) in a handful of restaurants. We provided you the ML related functionality, you need to expose this in an API for clients (the Kiosks).

**Your goal:** try to optimize the way you handle the requests, increase processing efficiency as much you can, in order to maximize the throughput of the system!

Here is in a nutshell what we simulate in this assignment:
 1. Each kiosks spawns at a restaurant. There is `TrainingData` that is specific to the restaurant (e.g. related to the products they sell).
 2. The `TrainingData` can be used to train a model. Here you will use the `fit_model()` function to train a classifier model.
 3. With the trained model, you can get predictions for new samples. In ML lingo we refer to this as "inference". In our example, the kiosk can have it's new samples
 classified in the service, that runs the `inference()` function at the backend.

We introduced some **simplifications** so that you don't need a powerful machine to solve this assignment:
 - Normally we work with RGB images (you can think of them as `H * W * 3` shaped uint8 arrays). This time we simplify this these to a 2D integer vectors.
 - We simulate the compute heavy ML calculations with `sleep()`.

## Working with the repo

First, please make a private fork of the repo, where you can make your changes and finally share your result. We ask you not to share original repo or your solution with anyone outside Deligo. Let's keep it fair for future applicants!

We provide you the following files under `src/`, please do not edit these:
 - `simulate_kiosks.py`: this simulates the kiosk, can be used with Locust.
 - `training.py`: ML training, import `fit_model()` to your solution from here.
 - `inference.py`: ML inference, import `inference()` from here.
 - `dataset.py` and `datatypes.py`: some support code for the used data types and dataset generation.

Your part:
 - `run_server.py`: Your code goes here, `run_server.py` should start your backend service on localhost.
 - Feel free to add anything else to the repo that you need for your solution.
 - You can use any openly available Python packages / modules / frameworks for your solution.
 - Please edit this readme (or add your own) to share details about your solution.

If you advance to the next round, you’ll have the opportunity to present your solution in-depth to the interviewing team, where you can discuss your approach, challenges, and any trade-offs you considered.


## The task

The goal of the assignment is to come up with a backend service that is optimized for request throughput. Essentially: try to maximize the number of requests that can be handled at a time (Requests / Sec). Consider the characteristics of the server load and the nature of the computations involved.

The service should expose a single endpoint: `/classify`. You can infer the request format from `src.simulate_kiosk.Kiosk.classify()`.
```
function classify: (query_input, training_data) -> classification_result
```

## Load testing

We will evaluate the performance using [Locust](https://locust.io/), the using following scenario

- 250 total number of users
- ramp up = 10 (users started / second)
- 180 sec total run time
- 5 distinct locations (see `simulate_kiosks.py`)

You can run this with the following command:
```bash
locust -f src/simulate_kiosks.py -H http://localhost:8000 Kiosk -u 250 -t 180s -r 10
```
