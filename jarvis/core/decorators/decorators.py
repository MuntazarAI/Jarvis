import functools
import time

def retry(max_attempts: int = 3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
            return None
        return wrapper
    return decorator

def timeout(seconds: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            if elapsed > seconds:
                raise TimeoutError(f"Execution took {elapsed}s, exceeded {seconds}s")
            return result
        return wrapper
    return decorator

def cache_result(ttl: int = 3600):
    cache = {}
    timestamps = {}
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            now = time.time()
            
            if key in cache and now - timestamps[key] < ttl:
                return cache[key]
            
            result = func(*args, **kwargs)
            cache[key] = result
            timestamps[key] = now
            return result
        return wrapper
    return decorator
