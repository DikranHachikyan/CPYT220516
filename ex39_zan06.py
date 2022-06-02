# 

def foo(arr = [], dc = {}):
    print(f'arr={arr} dc={dc}')
    print('--' * 25)
    n = len(arr)
    arr.append(n)
    dc[n] = n
    

if __name__ == '__main__':

    foo()
    foo([5,6,7], {'z':10, 'x':20})
    foo()
    foo([15,16,17], {'z':14, 'x':23})
    foo()

    print('---')
