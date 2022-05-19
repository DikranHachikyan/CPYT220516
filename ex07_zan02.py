# %%
conn = dict(
    host='localhost',
    db='northwind',
    port=1521,
    encoding='utf8',
    keepalive=True
)

print(conn['host'])

# %%

conn1 = ['northwind', 'localhost',  1521]

# northwind
# print(conn1[1])

# northwind
print(conn1[0])
# %%
# JSON - JavaScript Object Notation
user = {
    'firstname':'Anna',
    'lastname':'Smith',
    'age':30,
    'mails':['anna@no.com', 'smith@no.com']
}

print(user['firstname'])

# %%
type(user) is dict
# %%

user.keys()
# %%
user.values()

# %%
user.items()

# %%
'age' in user

# %%

print(user['phone'])

# %%

print(user.get('phone', '000-00-00'))

# %%
