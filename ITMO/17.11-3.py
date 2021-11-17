from typing import Callable


def logging(f: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print('Calling', f)
        return f(*args, **kwargs)

    return wrapper

@logging
def greet(msg):
    print(msg)

greet = logging(greet)
greet("YOOOOOOO!")
