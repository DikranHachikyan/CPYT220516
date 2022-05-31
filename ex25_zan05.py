sqrs = [ x ** 2 for x in range(11)]

print(f'values = {sqrs}')

txt = 'Lorem ipsum dolor sit'

letters = [ f'[{t}]' for t in txt]

print(f'letters = {letters}')

values = [ f'i={i} j={j}' for i in range(5) for j in range(5)]

# for i in range(5): 
#     for j in range(5):
#         ...

print(f'values = {values}')

print('---')
