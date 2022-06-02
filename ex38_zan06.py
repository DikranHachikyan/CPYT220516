# 

def foo(value, arr):
    value *= 2
    arr.append(value)

if __name__ == '__main__':

    v = 10
    lst = [4,5,6]

    foo(v, lst)

    print(f'v={v} lst={lst}')

    print('---')
