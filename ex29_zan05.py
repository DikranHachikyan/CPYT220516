# print(f'attribute name:{__name__}')
# port - глобална променлива
port = 8080

# 1. дефиниция на функцията

def add_numbers(a, b, d = 0):
    # тяло на функция
    # c - локална променлива
    c = a + b + d
    return c

if __name__ == '__main__':
    # 2. извикване на функция 
    v = add_numbers(5, 6)
    print(f'v={v}')

    x, y, w = 10, 25, 5
    z = add_numbers(x, y, w)
    print(f'{x} + {y} + {w}= {z}')

    print('---')
