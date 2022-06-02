# Глобални променливи

port = 22

def show():
    global port
    port = 3306 # лоша идея
    print(f'show port={port}')

if __name__ == '__main__':

    print(f'before port={port}')
    show()
    print(f'after port={port}')

    print('---')
