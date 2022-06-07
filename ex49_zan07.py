
from functools import wraps
from textwrap import wrap

def to_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [ f'{v}' for v in args]
        return func(*args, **kwargs)
    return wrapper

def add_brackets(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [ f'[{v}]' for v in args]
        return func(*args, **kwargs)
    return wrapper

@add_brackets
@to_string
def concat(*args, **kwargs):
    '''concatenate args with separator sep'''
    sep = kwargs.get('sep', ';')
    return sep.join(args)



if __name__ == '__main__':
    users = ['anna', 'maria','markus','jane']

    print(concat(*users))
    print(concat(*users, sep=' | '))

    values = [31,2,4,22,46]

    print(concat(*values, sep=','))

    print('---')
