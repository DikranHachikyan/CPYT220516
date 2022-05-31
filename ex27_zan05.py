# print(f'attribute name:{__name__}')
# 1. дефиниция на функцията

def add_numbers(a, b):
    # тяло на функция
    c = a + b
    print(f'{a} + {b} = {c}')

if __name__ == '__main__':
    # 2. извикване на функция 
    add_numbers(5, 6)

    x, y = 10, 25
    add_numbers(x, y)
    
    print('---')
