from fastapi import FastAPI

# Create a fastapi application instance
api = FastAPI()

# Define a Get endpoint at the route "/hello"

@api.get("hello")
def hello_world():

    return {"message": "Hellow World"}
