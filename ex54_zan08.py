
if __name__ == '__main__':
    
    actions = {
        '+': lambda a,b : a + b
    }

    try:
        value1 = float(input('first number:'))
        op = input('action (+):')
        value2 = float(input('second number:'))

        res = actions[op](value1, value2)
    except ValueError as e:
        print(f'Not a number!({e})')
    except KeyError as e:
        print(f'Invalid operation!({e})')
    except Exception as e:
        print(f'Unknown error!{e}')
    else:
        print(f'{value1} {op} {value2} = {res}')
        print('--- else ---')


    print('---')