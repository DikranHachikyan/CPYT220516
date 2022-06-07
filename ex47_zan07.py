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


def foo():
    sleep(0.3)

def bar():
    sleep(0.5)

def measure(func):
    t = time()
    func()
    print(f'{func.__name__}:{time() - t:.4f}')

if __name__ == '__main__':
    
    measure(foo)
    


    print('---')
