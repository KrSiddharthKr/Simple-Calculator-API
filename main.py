from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI(title="Simple Calculator API", version="1.0.0")

# A simple Python class (without Pydantic) , this shows why Pydantic is needed
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # Creating an object from the class
# person1 = Person("Alice", 25)
# person2 = Person("Alice", "not_a_number")
# print(person1.name)  # Alice
# print(person1.age)   # 25
# print(person2.name)  # Alice
# print(person2.age)   # 25

class CalculationRequest(BaseModel):
    a: int
    b: int
    operation: str
    precision: Optional[int] = 2
    
# METHOD - 1
# request = CalculationRequest(a=10, b=5, operation="add", precision=3)
# print(request.a)
# print(request.b)
# print(request.operation)
# print(request.precision)

# METHOD - 2
# data = {"a": "10", "b": "5", "operation": "add"}
# data = {"a": "10", "operation": "add"}
# request = CalculationRequest(**data)
# request.a = 345
# request.b = 9025
# print(request.a)
# print(request.b)
# print(request.operation)
# print(request.precision)

# print("Original:", request.a)

# # Now try to modify it
# try:
#     request.a = 999
#     print("Modified:", request.a)
# except Exception as e:
#     print("Error when trying to modify:", e)


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

@app.get("/calculate")
def calculate_query_parameters(a: int, b: int, operation: str):
    if operation == "add":
        result = a+b
    elif operation == "subtract":
        result = a-b
    elif operation == "multiply":
        result = a*b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = a/b
    else:
        raise HTTPException(status_code=400, detail=f"Invalid Operation: {operation}")
    
    return {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/calculate_optional")
def calculate_optional(a: int, b: int = 1, operation: Optional[str] = "add"):
    # b defaults to 1 if not provided
    # operation defaults to add if not provided
    
    if operation == "add":
        result = a+b
    elif operation == "subtract":
        result = a-b
    elif operation == "multiply":
        result = a*b
    elif operation == "divide":
        if b==0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = a/b
    else:
        raise HTTPException(status_code=400, detail=f"Invalid Operation: {operation}")
    
    return {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/calculate_advanced")
def calculate_advanced(a: int, b: int, operation: Optional[str] = "add"):
    valid_operations = ["add", "subtract", "multiply", "divide"]
    if operation not in valid_operations:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid operation: '{operation}'. Valid operations are: {valid_operations}"
        )
    
    if operation == "add":
        result = a+b
    elif operation == "subtract":
        result = a-b
    elif operation == "multiply":
        result = a*b
    elif operation == "divide":
        if b==0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = a/b
    
    return {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result,
        "valid_operations": valid_operations 
    }
    
# @app.post("/calculate")
