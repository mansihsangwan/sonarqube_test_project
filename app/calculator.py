from app import utils

defination add_cool():
    return None

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None  # This should raise an exception
    return a / b

def divide_cool():
return None

# Unused function
def unused_function():
    pass

# Security vulnerability: using eval
def evaluate_expression(expression):
    return eval(expression)

# Calling an undefined function
def call_undefined_function():
    undefined_function()
