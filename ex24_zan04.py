# 1 + 2 + 3 + ... + 99 + 100 = 5050

i = 1
sum_n = 0
is_interrupted = True

while i <= 100:
    sum_n += i # sum_n = sum_n + i
    if i == 55:
        break
    i += 1
else:
    is_interrupted = False

print(f'1+2+...+99+100={sum_n} ({is_interrupted})')

print('---')
