"""
Timing tools for intuition into the code's runtime complexity.
"""

import functools
import time


def time_me(f):
    """
    Takes a function as input, time the function when the
    function is called, log the time taken to the console.
    """

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        # Call the function.
        result = f(*args, **kwargs)

        end_time = time.time()
        time_taken = end_time - start_time

        print("Time taken (in seconds): ", time_taken)

        # Return the return value of the function call.
        return result
    
    return wrapper
