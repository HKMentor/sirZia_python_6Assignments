# Assignment 16:
'''Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().
'''
def log_function_call(func):
    def wrapper(name):
        print("Function is being called")
        return func(name)  
    return wrapper

@log_function_call
def say_hello(name):
    print(f"Hello {name}")

say_hello("Hooria")
