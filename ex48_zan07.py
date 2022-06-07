# 1.
# import time
# print(time.time())

# 1.1
# import time as tm
# print(tm.time())

# 2.
# from time import time as get_time, sleep
# print(get_time())

from time import time, sleep
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(f'{func.__name__}:{time() - t:.4f}')
    
    return wrapper

@measure
def foo(sleep_time=0.3):
    '''function foo sleeps sleep_time seconds'''
    sleep(sleep_time)



if __name__ == '__main__':
    
    foo(0.5)

    foo()
    
    print(f'name:{foo.__name__} doc:{foo.__doc__}')

    print('---')
