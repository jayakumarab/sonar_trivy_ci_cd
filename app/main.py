from fastapi import FastAPI
from app.calculator import add

app = FastAPI()


@app.get("/")
def home():
    return {"message": "FastAPI DevSecOps Project"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/add")
def addition(a: int, b: int):
    result = add(a, b)
    return {"result": result}