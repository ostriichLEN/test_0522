from fastapi import FastAPI

app = FastAPI()


def add_func(a, b):
    return a + b


def sub_func(a, b):
    # temp = 123
    return a - b


def mul_func(a: float, b: float) -> float:
    return a * b


@app.get("/")
def home():
    return {"status": "online", "message": "Welcome to the calculator API!"}


@app.get("/add")
def calculate_add(a: float, b: float):
    result = add_func(a, b)
    return {"operation": "addition", "a": a, "b": b, "result": result}
