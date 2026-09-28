'''Decorator -- > Functions that wrap other functions to add behavior without changing their code.'''

'''This is the #1 way "functions" show up in real production code: logging, timing, retry logic, caching (functools.lru_cache), auth checks in web 
frameworks (@login_required in Django/Flask), route registration in FastAPI (@app.get(...)).'''

import time
import functools

def timed(func):
    @functools.wraps(func)          # preserves func.__name__, docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timed
def fetch_data(n):
    return [i**2 for i in range(n)]

fetch_data(1000000)