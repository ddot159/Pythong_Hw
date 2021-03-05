import time
def calculate_time(func):
    """
    this is a function to calculate how long it takes for the decorator to
    compute the time
    """
    def wrapper():
        time_earlier = time_earlier.time()
        func()
        print(time_now - time_earlier)
    return wrapper

@calculate_time
def time():
    time_now = time_now.time()
    
