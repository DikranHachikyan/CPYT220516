# print(f'attribute name:{__name__}')

def show(title, *args, b, a = 100):
    print(f'title={title}')


    print('args:')
    for v in args:
        print(v, end =',')
    print()

    print(f'keyword only param b={b}')
    print(f'keyword only default param a={a}')

    print('.............')

if __name__ == '__main__':

    show('First Param 1', 1, 2, 3, 4, b = 5, a = 10)


    show('First Param 2', 1, 2, 3, 4, b = 33)


    show('First Param 3', b=40)
    


    print('---')
