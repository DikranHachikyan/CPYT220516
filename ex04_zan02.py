# %%
s1 = 'Lorem ipsum dolor sit amet'

s2 = "Lorem ipsum dolor sit"
# %%
s3 = '''Lorem ipsum dolor sit amet,
consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna
aliqua.'''

print(s3)
# %%
def foo():
    '''Function foo()
    print Hello Foo

    author: me
    created: 18.05.2022'''
    
    print('Hello Foo!')
    

# %%
foo()
# %%
print(foo.__doc__)
# %%

order_amt = 530.0
vat = 1.2

print(f'Your order amt: {order_amt * vat:.3f}')
# %%
s1[4]
# %%
s1[0:5]
# %%
s1[0:20:2]
# %%
s1.upper()


# %%
