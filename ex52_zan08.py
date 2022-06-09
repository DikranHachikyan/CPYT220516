
from functools import wraps


def to_upper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func

        args = [ f'{v}'.upper() for v in args]
        # args = [ v.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    

    print('Hello Python', 'Java', 'lorem', 'ipsum')

    print = to_upper(print)
  
    print('Hello Python', 'Java', 'lorem', 'ipsum')
    print(12, 'Java', 30, 'lorem', 'ipsum')

    
    print = print.__original
    
    print('Hello Python', 'Java', 'lorem', 'ipsum')

    print('---')
