# Глобални променливи

port = 22

def show():
    port = 3306
    print(f'show port={port}')

if __name__ == '__main__':

    print(f'before port={port}')
    show()
    print(f'after port={port}')

    print('---')
