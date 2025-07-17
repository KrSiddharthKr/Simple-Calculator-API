from fastapi import FastAPI, HTTPException

app = FastAPI(title="Simple Calculator API", version="1.0.0")

@app.get("/")
def read_root():
    return {
        "message": "Welcome to simple calculator API",
        "endpoints": [
            "/add/{a}/{b}",
            "/subtract/{a}/{b}",
            "/multiply/{a}/{b}",
            "/divide/{a}/{b}"
        ]
    }

@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    result = a + b
    return {
        "operation": "addition",
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/subtract/{a}/{b}")
def subtract_numbers(a: int, b: int):
    result = a-b
    return {
        "operation": "subtraction",
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/multiply/{a}/{b}")
def multiply_numbers(a: int, b: int):
    result = a*b
    return {
        "operation": "multiplication",
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/divide/{a}/{b}")
def divide_numbers(a: int, b: int):
    if b==0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    
    result = a/b
    return {
        "operation": "division",
        "a": a,
        "b": b,
        "result": result
    }
    
@app.get("/int_divide/{a}/{b}")
def integer_division(a: int, b: int):
    if b==0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    quotient = a//b
    remainder = a%b
    return {
        "operation": "integer_division",
        "a": a,
        "b": b,
        "quotient": quotient,
        "remainder": remainder
    } 