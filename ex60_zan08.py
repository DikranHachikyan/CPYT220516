class ConnectionInfoError(Exception):
    pass


def print_key(key, **kwargs):
    
    if key not in kwargs:
        raise ConnectionInfoError(f'Please check ...{key}')
    
    print(f'{key} => {kwargs[key]}')
    

if __name__ == '__main__':
    
    conn = {
        'host':'localhost',
        'port':1521,
        'service':'oracle'
    }

    try:
        print_key('host', **conn)
        print_key('ip', **conn)
    except ConnectionInfoError as e:
        # pass
        print(f'invalid key:{e}')

    print('---')