# %%
tpl = (11,22,33,44,66)
# %%

print(tpl[1])
# %%
tpl[1] = 100

# %%

a, b, c, d, e = tpl

print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}')

# %%

a, b, *_ = tpl

print(f'a = {a}, b = {b}')


# %%

*_, a, b = tpl

print(f'a = {a}, b = {b}')


# %%

tpl = 1,2,3,4,5

print(tpl)

# %%

3 in tpl

# %%

t = (10,)

# %%
type(t) is tuple

# %%
