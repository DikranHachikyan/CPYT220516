# print(f'attribute name:{__name__}')

def show(title, a = 100, *args, **kwargs):
    print(f'title={title}')

    print(f'optional param a={a}')

    print('args:')
    for v in args:
        print(v, end =',')
    print()

    print('kwargs')
    kw = {
        's': kwargs.get('service'),
        'db': kwargs.get('db','test')

    }    

    print(f'kw={kw}')
    print('.............')

if __name__ == '__main__':
    # 1.
    # show('Text Editor')
    # 2.
    # show('Text Editor', 20)
    # 3.
    show('Text Editor', 20, 1,2,3,4) 
    
    app = {
        'service':'oracle',
        'port':1521
        # 'db': 'northwind'
    }
    show('Text Editor', 20, 1,2,3,4, **app)


    show('Text Editor', 20, 1,2,3,4, db='sales', service='mysql') 


    print('---')
