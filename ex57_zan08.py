def print_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError as e:
        # 3. добро решение
        raise

        # 2. вариант 2 (не е добро решение)
        # pass

        # 1. вариант 1 (не е добро решение)
        # print(f'invalid key:{key}')

if __name__ == '__main__':
    
    conn = {
        'host':'localhost',
        'port':1521,
        'service':'oracle'
    }

    print_key('host', **conn)
    print_key('ip', **conn)

    print('---')