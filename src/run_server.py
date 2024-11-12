############################################
# TODO:
# Your task is to implement the server
# that can handle the requests from the clients.
# Expose the `classify` endpoint that takes
# `TrainingData` and `QueryInput` as input and
# returns `ClassificationResult`. See how
# simulating_kiosks.py calls the server.
############################################
import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get('/ping')
def ping():
    return PlainTextResponse('OK')


if __name__ == '__main__':
    uvicorn.run(app, port=8888)

