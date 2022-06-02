# print(f'attribute name:{__name__}')

def show(title, *, b, a = 100):
    print(f'title={title}')

    print(f'keyword only param b={b}')
    print(f'keyword only default param a={a}')

    print('.............')

if __name__ == '__main__':

    show('First Param 1', b = 5, a = 10)


    print('---')
