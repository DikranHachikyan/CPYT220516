# 
# 
def add_numbers(n):
    print(f'n={n}')
    if n > 0:
        return n + add_numbers(n - 1)
    return 0

if __name__ == '__main__':

    res = add_numbers(5)
    print(f'res = {res}')
    print('---')
