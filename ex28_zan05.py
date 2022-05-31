# print(f'attribute name:{__name__}')
# port - глобална променлива
port = 8080

# 1. дефиниция на функцията

def add_numbers(a, b):
    # тяло на функция
    # c - локална променлива
    c = a + b
    return c

if __name__ == '__main__':
    # 2. извикване на функция 
    v = add_numbers(5, 6)
    print(f'v={v}')

    x, y = 10, 25
    z = add_numbers(x, y)
    print(f'{x} + {y} = {z}')

    print('---')
