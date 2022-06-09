
if __name__ == '__main__':
    
    actions = {
        '+': lambda a,b : a + b
    }
    while True:
        try:
            op = input('action (+, q-quit):')
            
            if op == 'q':
                # break
                quit()

            value1 = float(input('first number:'))
            value2 = float(input('second number:'))

            res = actions[op](value1, value2)
        except (ValueError, KeyError) as e:
            print(f'Not a number or invalid operation!({e})')
        except Exception as e:
            print(f'Unknown error!{e}')
        else:
            print(f'{value1} {op} {value2} = {res}')
            print('--- else ---')
            continue
        finally:
            print('--- finally ---')

    print('---')