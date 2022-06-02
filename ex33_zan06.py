# print(f'attribute name:{__name__}')

def show(title, a = 100, *args):
    print(f'title={title}')

    print(f'optional param a={a}')

    print('args:')
    for v in args:
        print(v, end =',')
    print()

    print('.............')

if __name__ == '__main__':

    show('First Param 1', 10, 1, 2, 3, 4)


    show('First Param 2', 1, 2, 3, 4)


    show('First Param 3')
    


    print('---')
